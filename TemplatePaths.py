import os

import Utils

root = Utils.get_jessica_root()
template_dir = os.path.join(root, "templates")
component_dir = os.path.join(template_dir, "component")

index_file = os.path.join(template_dir, "index.html")
init_file = os.path.join(template_dir, "init.js")

html_path = os.path.join(component_dir, "component.html")
js_path =  os.path.join(component_dir, "component.js")
css_path =  os.path.join(component_dir, "component.css")
json_path =  os.path.join(component_dir, "component.json")