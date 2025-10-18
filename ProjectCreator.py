import os

import Utils
import TemplatePaths
from FileHelpers import create_file
from ComponentCreator import create_component

root = Utils.get_jessica_root()

def create_project(name: str) -> None:
    # Create the index file
    sub_data = {
        "Name": name # Not the component's name - The component it points to
    }

    def_name = "app"
    create_file(def_name, ".", TemplatePaths.index_file, "html", sub_data)
    create_file(def_name, ".", TemplatePaths.css_path, "css")
    create_file("component", ".", TemplatePaths.json_path, "json", {
        "name": def_name,
        "tag": def_name
    })

    create_file("init", ".", TemplatePaths.init_file, "js", sub_data)
    create_component(name, ".")

    #create_file("app", ".", TemplatePaths.js_path, "js")
