import os

import Utils
from FileHelpers import create_file

root = Utils.get_jessica_root()
template_dir = os.path.join(root, "templates")
component_dir = os.path.join(template_dir, "component")

html_path = os.path.join(component_dir, "component.html")
js_path =  os.path.join(component_dir, "component.js")
css_path =  os.path.join(component_dir, "component.css")
json_path =  os.path.join(component_dir, "component.json")

def create_component( name: str, location: str ) -> None:
    target_dir = os.path.join(location, name)

    os.mkdir(target_dir)

    create_file(name, target_dir, html_path, "html")
    create_file(name, target_dir, js_path, "js")
    create_file(name, target_dir, css_path, "css")
    create_file("component", target_dir, json_path, "json")
