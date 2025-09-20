import ProjectCreator
import ComponentCreator
import FileHelpers
from JessicaParser import parse_html
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



## Complex Code
 ##
   ##

def properly_load_comps(current_element: HtmlElement,
        unloaded_components: dict[str, HtmlElement],
        loaded_components: dict[str, HtmlElement]):
    
    # Properly load any unloaded componenents (recursive)
    if current_element.name in unloaded_components:
        if current_element.name not in loaded_components:
            comp = stitch_components(unloaded_components[current_element.name], unloaded_components, loaded_components)
            loaded_components[current_element.name] = comp

        target_element = loaded_components[current_element.name].clone()
    else:
        target_element: HtmlElement = HtmlElement(current_element.name)
    
    return target_element
    
def append_all_chilren(from_elem: HtmlElement, to_elem: HtmlElement):
    for child in from_elem.children:
        to_elem.children.append(child)


def stitch_components(current_element: HtmlElement,
        unloaded_components: dict[str, HtmlElement],
        loaded_components: dict[str, HtmlElement]):
    
    target_element = properly_load_comps(current_element, unloaded_components, loaded_components)
    target_element.data = current_element.data

    for child in current_element.children:
        complete_elem = stitch_components(child, unloaded_components, loaded_components)
        append_all_chilren(complete_elem, target_element)
        
    return target_element

   ##
 ##
##

def load_component_html(component_info: dict[str, componentInfo]):
    components: dict[str, HtmlElement] = {}
    for ci in component_info:
        cp = component_info[ci]
        if cp.ComponentName not in components:
            loaded_html: str = FileHelpers.load_file(os.path.join(cp.DirPath, f'{cp.ComponentName}.html'))
            components[cp.ComponentName] = parse_html(loaded_html)
    return components

def run_jessica():
    comps = get_components(".")
    unloaded_components: dict[HtmlElement] = load_component_html(comps)
    loaded_components: dict[HtmlElement] = {}

    html = FileHelpers.load_file("./templates/index.html")
    tree: HtmlElement = parse_html(html)

    rar = stitch_components(tree, unloaded_components, loaded_components)
    #print(loaded_components)

def main():
    run_jessica()

if __name__ == '__main__':
    #ComponentCreator.create_component("Jess", ".")
    main()
