#!/bin/bash

# Define the units and their directories
units=("Unit1" "Unit2" "Unit3" "Unit4" "Unit5" "Unit6" "Unit7")

# Add all HTML files from each unit directory to git
for unit in "${units[@]}"; do
  git add "${unit}/*.ipynb"
  git add "${unit}/*.html"
  git add "${unit}/figures/*"
done

# Commit the changes with a meaningful commit message
git commit -m "Lesson files for all units"

# Push the changes to the remote repository
git push

echo "HTML files added and changes pushed to GitHub successfully."