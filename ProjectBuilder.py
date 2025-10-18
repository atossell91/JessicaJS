import os
import shutil

from ComponentStitcher import stich_component
from HtmlWriter import write_html
from JComponent import load_component

def build_project(components_dir, output_dir):
    #tree = stitch_project(index_filepath, components_dir)
    comp = load_component(components_dir)
    tree = stich_component(comp)
    html = write_html(tree)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    js_src = os.path.join(components_dir, "init.js")
    js_tgt = os.path.join(output_dir, "init.js")
    shutil.copy(js_src, js_tgt)
    
    filepath = os.path.join(output_dir, "index.html")
    with open(filepath, "w") as file:
        file.write(html)