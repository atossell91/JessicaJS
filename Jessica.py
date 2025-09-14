import ProjectCreator
import ComponentCreator
import FileHelpers
import JessicaParser
import html.parser
import re
import os
import json
from ComponentInfo import componentInfo
from HtmlElement import HtmlElement
from typing import Iterator

def contains_file(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

def replace(content, tag_name, body):
    full_tag = f'<{tag_name}/>'

def CreateComponentInfo(dir_path: str) -> componentInfo:
    name: str = dir_path
    manifest_path: str = os.path.join(dir_path, "component.json")

    with open(manifest_path, 'rb') as f:
        obj: dict[str, str] = json.load(f)

    if "name" in obj:
        name = obj["name"]

    info = componentInfo(name, dir_path)
    return info
    

def get_components(path: str) -> dict[str, componentInfo]:
    component_dirs = {}
    contents = os.listdir(path)
    for item in contents:
        if os.path.isdir(item) and contains_file(item, "component.json"):
            comp = CreateComponentInfo(item)
            if comp.ComponentName not in component_dirs:
                component_dirs[comp.ComponentName] = comp
    return component_dirs

def process_node(node: HtmlElement, components: set[componentInfo]) -> None:
    if node.name in components:
        pass

def bfs(node):
    for child in node.children:
        print(child.name)
        bfs(child)

def bbw(current_element: HtmlElement,
        unloaded_components: dict[str, HtmlElement],
        loaded_components: dict[str, HtmlElement]):
    
    if current_element.name in unloaded_components:
        if current_element.name not in loaded_components:
            comp = bbw(unloaded_components[current_element.name], unloaded_components, loaded_components)
            loaded_components[current_element.name] = comp

        target_element = loaded_components[current_element.name].clone()
    else:
        target_element: HtmlElement = HtmlElement(current_element.name)
    
    target_element.data = current_element.data

    for child in current_element.children:
        target_element.children.append(bbw(child, unloaded_components, loaded_components))
    return target_element

def parse_html(html_content: str):
    pass

def run_jessica():
    comps = get_components(".")

    parser = JessicaParser.JessicaParser()

    html = FileHelpers.load_file("./templates/index.html")
    parser.parse(html)
    tree: HtmlElement = parser.flush()
    bfs(tree)

def main():
    run_jessica()

if __name__ == '__main__':
    #main()
    ComponentCreator.create_component("Jess", ".")