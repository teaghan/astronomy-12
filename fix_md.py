import os
import shutil
import re

def copy_and_rename_readme_files(unit_dirs, md_dir):
    """
    Copies all README.md files from the Unit* directories into the md_files directory,
    renames them to match the unit structure (e.g., md_files/Unit1_README.md),
    adjusts embedded links, and fixes image paths to point to the correct locations.
    """
    link_pattern = re.compile(r'\[(.*?)\]\((https://github.com/teaghan/astronomy-12/tree/main/Unit\d+/(.*?))\.ipynb\)')
    image_pattern = re.compile(r'!\[(.*?)\]\(\./figures/(.*?)\)')

    for unit_dir in unit_dirs:
        readme_path = os.path.join(unit_dir, "README.md")
        if os.path.exists(readme_path):
            # Extract the unit number from the directory name (e.g., Unit1 -> Unit1_README.md)
            unit_name = os.path.basename(unit_dir)
            new_readme_name = f"{unit_name}_README.md"
            new_readme_path = os.path.join(md_dir, new_readme_name)
            
            # Read the README.md file content
            with open(readme_path, "r") as file:
                content = file.read()
            
            # Adjust the links
            new_content = link_pattern.sub(r'[\1](../md_files/\3.html)', content)
            
            # Adjust the image paths
            new_content = image_pattern.sub(r'![\1](../{}/figures/\2)'.format(unit_name), new_content)
            
            # Write the modified content to the new README file
            with open(new_readme_path, "w") as file:
                file.write(new_content)
            
            print(f"Copied and adjusted {readme_path} to {new_readme_path}")

def copy_and_adjust_main_readme(main_readme, output_file):
    """
    Copies the main README.md file to index.md and adjusts embedded links to point to the correct paths.
    Also adds the appropriate header.
    """
    # Regex patterns for various adjustments
    link_pattern = re.compile(r'\[(.*?)\]\((https://github.com/teaghan/astronomy-12/tree/main/Unit\d+/(.*?))\.ipynb\)')
    unit_link_pattern = re.compile(r'\[(.*?)\]\((https://github.com/teaghan/astronomy-12/tree/main/(Unit\d+))\)')
    
    if os.path.exists(main_readme):
        # Read the main README.md file content
        with open(main_readme, "r") as file:
            content = file.read()
        
        # Adjust the notebook links
        new_content = link_pattern.sub(r'[\1](./md_files/\3.html)', content)
        
        # Adjust the unit directory links to point to the corresponding README.html files
        new_content = unit_link_pattern.sub(r'[\1](./md_files/\3_README.html)', new_content)
        
        # Prepend the header for index.md
        new_content = "---\nlayout: home_default\n---\n\n" + new_content
        
        # Write the modified content to index.md
        with open(output_file, "w") as file:
            file.write(new_content)
        
        print(f"Copied and adjusted {main_readme} to {output_file}")

def add_layout_to_md_files(md_dir):
    """
    Adds the specified layout lines to the beginning of each markdown file in the md_files directory.
    """
    layout_lines = "---\nlayout: embed_default\n---\n\n"
    
    for root, dirs, files in os.walk(md_dir):
        for file_name in files:
            if file_name.endswith(".md"):
                md_file_path = os.path.join(root, file_name)
                
                # Read the existing content of the file
                with open(md_file_path, "r") as file:
                    content = file.read()
                
                # Prepend the layout lines to the content
                new_content = layout_lines + content
                
                # Write the modified content back to the file
                with open(md_file_path, "w") as file:
                    file.write(new_content)
                
                print(f"Added layout to {md_file_path}")

if __name__ == "__main__":
    # Define the directories
    unit_dirs = [d for d in os.listdir() if os.path.isdir(d) and d.startswith("Unit")]
    md_dir = "md_files"
    main_readme = "README.md"
    output_index_file = "index.md"

    # Ensure the md_files directory exists
    if not os.path.exists(md_dir):
        os.makedirs(md_dir)

    # Perform the tasks
    copy_and_rename_readme_files(unit_dirs, md_dir)
    copy_and_adjust_main_readme(main_readme, output_index_file)
    add_layout_to_md_files(md_dir)

    print("All markdown files processed successfully.")
