import os
import sys
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
from nbconvert.preprocessors import Preprocessor

class RemoveEmptyCellsPreprocessor(Preprocessor):
    def preprocess(self, nb, resources):
        # Filter out any cells that are empty
        nb.cells = [cell for cell in nb.cells if cell.source.strip() != ""]
        return nb, resources

def convert_notebooks_to_markdown(notebook_paths, output_dir):
    # Create the Markdown exporter with the custom preprocessor
    exporter = MarkdownExporter()
    exporter.register_preprocessor(RemoveEmptyCellsPreprocessor, enabled=True)
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Process each notebook
    for notebook_path in notebook_paths:
        with open(notebook_path, 'r') as nb_file:
            nb_content = nbformat.read(nb_file, as_version=4)
        
        # Convert notebook to markdown
        (body, resources) = exporter.from_notebook_node(nb_content)
        
        # Define output path
        notebook_name = os.path.splitext(os.path.basename(notebook_path))[0]
        output_path = os.path.join(output_dir, f"{notebook_name}.md")
        
        # Save the converted markdown
        with open(output_path, 'w') as md_file:
            md_file.write(body)
        
        print(f"Converted {notebook_path} to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_notebooks_to_markdown.py <notebook1.ipynb> <notebook2.ipynb> ... <output_dir>")
        sys.exit(1)
    
    # The last argument is the output directory
    output_dir = sys.argv[-1]
    
    # All preceding arguments are notebook paths
    notebook_paths = sys.argv[1:-1]
    
    convert_notebooks_to_markdown(notebook_paths, output_dir)
