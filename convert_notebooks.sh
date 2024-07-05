#!/bin/bash

# Loop through each Unit directory
for unit_dir in Unit*; do
  # Check if the directory exists and is a directory
  if [ -d "$unit_dir" ]; then
    # Find all .ipynb files in the directory, excluding *-checkpoint.ipynb files, and convert them to HTML
    find "$unit_dir" -name "*.ipynb" ! -name "*-checkpoint.ipynb" -exec jupyter nbconvert --to html {} --output-dir="$unit_dir" \;
  fi
done

echo "HTML files created successfully."
