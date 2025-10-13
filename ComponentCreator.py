import os

import TemplatePaths
from FileHelpers import create_file

def create_component( name: str, location: str ) -> None:
    target_dir = os.path.join(location, name)

    os.mkdir(target_dir)

    create_file(name, target_dir, TemplatePaths.html_path, "html")
    create_file(name, target_dir, TemplatePaths.js_path, "js", {"name": name})
    create_file(name, target_dir, TemplatePaths.css_path, "css")
    create_file("component", target_dir, TemplatePaths.json_path, "json", {"name": name, "tag": name}) # type: ignore
