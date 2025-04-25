#!/bin/bash

# List of critical services to monitor
SERVICES=("ssh" "cron" "nginx" "mysql")

# Log file
LOG_FILE="/var/log/service_checker.log"

# Ensure log file exists
touch "$LOG_FILE"

# Timestamp
echo "===== $(date) =====" >> "$LOG_FILE"

# Function to check each service
check_services() {
  for service in "${SERVICES[@]}"; do
    STATUS=$(systemctl is-active "$service")
    if [[ "$STATUS" != "active" ]]; then
      echo "[$service] Status: $STATUS" | tee -a "$LOG_FILE"
      # Optional alert: desktop notification (Linux GUI)
      if command -v notify-send &> /dev/null; then
        notify-send "Service Alert" "$service is $STATUS"
      fi
    else
      echo "[$service] Status: $STATUS" >> "$LOG_FILE"
    fi
  done
  echo "" >> "$LOG_FILE"
}

# Run the check
check_services
