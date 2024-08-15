import os
import re
from PyPDF2 import PdfReader

def sort_files(files):
    """
    Sort files to ensure that UnitX_README.md files come first,
    followed by numbered markdown files like 1_1*.md, 1_2*.md, etc.
    """
    # Separate files into two groups: UnitX_README.md and numbered markdown files
    unit_readme_files = sorted([f for f in files if re.match(r'Unit\d+_README\.md', f)])
    numbered_md_files = sorted([f for f in files if re.match(r'\d+_\d+.*\.md', f)])

    # Combine both lists
    num_units = len(unit_readme_files)
    sorted_files = unit_readme_files + numbered_md_files
    return sorted_files, num_units

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using PyPDF2.
    """
    pdf_text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PdfReader(file)
            for page in reader.pages:
                pdf_text += page.extract_text()
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
    return pdf_text

def combine_markdown_and_pdf_files(md_dir, output_file):
    # Get all markdown files in the input directory
    md_files = [f for f in os.listdir(md_dir) if f.endswith('.md')]
    
    # Sort files in the desired order
    sorted_files, num_units = sort_files(md_files)
    
    # Combine the content of all sorted markdown files into one file
    with open(output_file, 'w') as outfile:
        for filename in sorted_files:
            filepath = os.path.join(md_dir, filename)
            with open(filepath, 'r') as infile:
                content = infile.read()
                outfile.write(f"# {filename}\n")  # Optionally add filename as a section header
                outfile.write(content)
                outfile.write("\n\n")  # Add a newline between files for readability
            print(f"Added {filename} to {output_file}")

        # Now handle the assignments (PDF files)
        for unit_number in range(1, num_units + 1):
            pdf_path = f"Unit{unit_number}/Unit{unit_number}_Assignment.pdf"
            print(pdf_path)
            if os.path.exists(pdf_path):
                print(f"Extracting text from {pdf_path}...")
                pdf_text = extract_text_from_pdf(pdf_path)
                pritn(pdf_text)
                outfile.write(f"\n# Unit {unit_number} Assignment\n")
                outfile.write(pdf_text)
                outfile.write("\n\n")  # Add a newline between content sections for readability
            else:
                print(f"Assignment PDF not found for Unit {unit_number}: {pdf_path}")

if __name__ == "__main__":
    input_directory = "./md_files"
    output_file_path = "./course_content.txt"
    
    combine_markdown_and_pdf_files(input_directory, output_file_path)
    print(f"All markdown and PDF contents combined into {output_file_path}")
