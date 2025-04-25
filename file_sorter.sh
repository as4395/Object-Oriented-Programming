#!/bin/bash

# Default folder is Downloads if none is given
TARGET_DIR="${1:-$HOME/Downloads}"

# Define file type groups
declare -A TYPES
TYPES["Images"]="jpg jpeg png gif bmp svg"
TYPES["Documents"]="pdf doc docx txt odt xls xlsx ppt pptx"
TYPES["Videos"]="mp4 mkv avi mov flv wmv"
TYPES["Archives"]="zip tar.gz tar.bz2 rar 7z"
TYPES["Audio"]="mp3 wav flac m4a ogg"
TYPES["Scripts"]="sh py js pl rb php"

# Function to create and move files
organize_files() {
  cd "$TARGET_DIR" || exit
  echo "Organizing files in: $TARGET_DIR"

  for category in "${!TYPES[@]}"; do
    EXTENSIONS=${TYPES[$category]}
    mkdir -p "$category"

    for ext in $EXTENSIONS; do
      mv *."$ext" "$category/" 2>/dev/null
    done
  done

  echo "Done organizing!"
}

# Function to delete empty folders
clean_empty_dirs() {
  find "$TARGET_DIR" -type d -empty -delete
  echo "Empty folders cleaned up."
}

# Ask for cleanup
read -p "Delete empty folders afterward? (y/n): " choice

organize_files
[[ "$choice" == "y" || "$choice" == "Y" ]] && clean_empty_dirs
