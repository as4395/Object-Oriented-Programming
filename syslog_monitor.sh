#!/bin/bash

# File to store logs
LOG_FILE="/var/log/system_monitor.log"

# Check if the script has the right permissions
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root to write to $LOG_FILE"
  exit
fi

# Create the log file if it doesn't exist
touch $LOG_FILE

# Function to get CPU usage
get_cpu_usage() {
  top -bn1 | grep "Cpu(s)" | awk '{print "CPU Usage: " $2 + $4 "%"}'
}

# Function to get memory usage
get_memory_usage() {
  free -m | awk 'NR==2{printf "Memory Usage: %.2f%%\n", $3*100/$2 }'
}

# Function to get disk usage
get_disk_usage() {
  df -h | awk '$NF=="/"{printf "Disk Usage: %s\n", $5}'
}

# Function to get network usage
get_network_usage() {
  RX=$(cat /sys/class/net/eth0/statistics/rx_bytes)
  TX=$(cat /sys/class/net/eth0/statistics/tx_bytes)
  sleep 1
  RX2=$(cat /sys/class/net/eth0/statistics/rx_bytes)
  TX2=$(cat /sys/class/net/eth0/statistics/tx_bytes)
  echo "Network RX: $((($RX2 - $RX)/1024)) KB/s, TX: $((($TX2 - $TX)/1024)) KB/s"
}

# Monitoring loop
while true; do
  echo "------ $(date) ------" | tee -a $LOG_FILE
  get_cpu_usage | tee -a $LOG_FILE
  get_memory_usage | tee -a $LOG_FILE
  get_disk_usage | tee -a $LOG_FILE
  get_network_usage | tee -a $LOG_FILE
  echo "" | tee -a $LOG_FILE
  sleep 5
done
