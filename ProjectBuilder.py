import os

from ComponentStitcher import stitch_project
from HtmlWriter import write_html

def build_project(index_filepath, components_dir, output_dir):
    tree = stitch_project(index_filepath, components_dir)
    html = write_html(tree)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    filepath = os.path.join(output_dir, "index.html")
    with open(filepath, "w") as file:
        file.write(html)