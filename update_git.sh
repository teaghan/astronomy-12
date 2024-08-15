#!/bin/bash

# Define the units and their directories
units=("Unit1" "Unit2" "Unit3" "Unit4" "Unit5" "Unit6" "Unit7")

# Add all Units, ignoring checkpoint files and directories
for unit in "${units[@]}"; do
  find "${unit}" -type f \( -name "*.ipynb" -o -name "*.html" \) ! -name "*-checkpoint.ipynb" ! -path "*/.ipynb_checkpoints/*" -exec git add {} \;
  git add "${unit}/figures/*"
  git add "${unit}/README.md"
  git add "${unit}/*.docx"
  git add "${unit}/*.pdf"
done

git add "images/*"
git add "html_lessons/*"
git add "md_files/*"
git add "_layouts/*"
git add "_sass/*"
git add "_includes/*"
git add "assets/*"
git add "Assistant_Instructions.txt"
git add "Tutor_Instructions.txt"
git add "bc_science_curriculum.txt"
git add "README.md"
git add "_config.yml"
git add "index.md"
git add "fix_md.py"
git add "nb_to_md.py"
git add "combine_content.py"
git add "course_content.txt"
git add "convert_notebooks.sh"
git add "update_git.sh"

# Commit the changes with a meaningful commit message
git commit -m "General file update."

# Push the changes to the remote repository
git push

echo "HTML files added and changes pushed to GitHub successfully."