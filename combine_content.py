import os
import re

def sort_files(files):
    """
    Sort files to ensure that UnitX_README.md files come first,
    followed by numbered markdown files like 1_1*.md, 1_2*.md, etc.
    """
    # Separate files into two groups: UnitX_README.md and numbered markdown files
    unit_readme_files = sorted([f for f in files if re.match(r'Unit\d+_README\.md', f)])
    numbered_md_files = sorted([f for f in files if re.match(r'\d+_\d+.*\.md', f)])

    # Combine both lists
    sorted_files = unit_readme_files + numbered_md_files
    return sorted_files

def combine_markdown_files(input_dir, output_file):
    # Get all markdown files in the input directory
    md_files = [f for f in os.listdir(input_dir) if f.endswith('.md')]
    
    # Sort files in the desired order
    sorted_files = sort_files(md_files)
    
    # Combine the content of all sorted markdown files into one file
    with open(output_file, 'w') as outfile:
        for filename in sorted_files:
            filepath = os.path.join(input_dir, filename)
            with open(filepath, 'r') as infile:
                content = infile.read()
                outfile.write(f"# {filename}\n")  # Optionally add filename as a section header
                outfile.write(content)
                outfile.write("\n\n")  # Add a newline between files for readability
            print(f"Added {filename} to {output_file}")

if __name__ == "__main__":
    input_directory = "./md_files"
    output_file_path = "./course_content.txt"
    
    combine_markdown_files(input_directory, output_file_path)
    print(f"All markdown files combined into {output_file_path}")