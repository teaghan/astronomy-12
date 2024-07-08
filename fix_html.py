import os
import re
import argparse

def convert_display_math(content):
    # Convert double $$...$$ to \[...\]
    return re.sub(r'\$\$(.+?)\$\$', r'\\[\1\\]', content, flags=re.DOTALL)

def convert_inline_math(content):
    # Convert single $...$ to \( ... \), ensuring not to affect already converted \[...\]
    return re.sub(r'(?<!\\)\$(?!\$)(.+?)(?<!\\)\$(?!\$)', r'\\(\1\\)', content)

def replace_mathjax_config(content):
    new_mathjax_config = """
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        TeX: {
            equationNumbers: {
                autoNumber: "AMS",
                useLabelIds: true
            }
        },
        tex2jax: {
            inlineMath: [ ['\\\\\(','\\\\\)']],
            displayMath: [ ['\\\\\[','\\\\\]']],
            processEscapes: true,
            processEnvironments: true
        },
        displayAlign: 'center',
        CommonHTML: {
            linebreaks: {
                automatic: true
            }
        }
    });
    MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
</script>
<!-- End of mathjax configuration --><script type="module">
"""
    # Use regex to match and replace the existing MathJax configuration
    pattern = re.compile(r'<!-- Load mathjax -->.*?<!-- End of mathjax configuration --><script type="module">', re.DOTALL)
    return pattern.sub(new_mathjax_config, content)

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = convert_display_math(content)
    content = convert_inline_math(content)
    content = replace_mathjax_config(content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    parser = argparse.ArgumentParser(description='Process HTML files to convert math delimiters and update MathJax configuration.')
    parser.add_argument('directory', type=str, help='Directory containing HTML files')
    args = parser.parse_args()

    directory = args.directory

    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            process_file(os.path.join(directory, filename))

if __name__ == '__main__':
    main()
