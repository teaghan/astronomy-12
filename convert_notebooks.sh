#!/bin/bash

# Remove old output directories if they exist
rm -r html_lessons/
rm -r md_files/

# Create new output directories
mkdir html_lessons/
mkdir md_files/

# Loop through each Unit directory
for unit_dir in Unit*; do
  # Check if the directory exists and is a directory
  if [ -d "$unit_dir" ]; then
    # Find all .ipynb files in the directory, excluding *-checkpoint.ipynb files, and convert them to HTML
    find "$unit_dir" -name "*.ipynb" ! -name "*-checkpoint.ipynb" -exec jupyter nbconvert --to html {} --output-dir="./html_lessons/" \;

    # Convert the same notebooks to markdown using the custom preprocessor to remove empty cells
    notebook_files=$(find "$unit_dir" -name "*.ipynb" ! -name "*-checkpoint.ipynb")
    if [ ! -z "$notebook_files" ]; then
      python nb_to_md.py $notebook_files "./md_files/"
    fi
    
    # Run the Python script to fix HTML files (if needed)
    python fix_html.py "./html_lessons/"
  fi
done

python fix_md.py
python combine_content.py 

echo "HTML and Markdown files created successfully."
