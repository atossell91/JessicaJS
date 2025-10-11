import os
import json

import FileHelpers

from ComponentInfo import componentInfo
from HtmlElement import HtmlElement
from JessicaParser import parse_html

def contains_file(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

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

def affirm(current_element: HtmlElement,
        unloaded_components: dict[str, HtmlElement],
        loaded_components: dict[str, HtmlElement]):

    if current_element.name in unloaded_components:
        new_node = affirm(unloaded_components[current_element.name], unloaded_components, loaded_components)
    else:
        new_node: HtmlElement = HtmlElement(current_element.name)
        new_node.data = current_element.data
        new_node.attributes = current_element.attributes

    for child in current_element.children:
        temp_node = affirm(child, unloaded_components, loaded_components)
        if temp_node.name == 'root':
            for temp_child in temp_node.children:
                new_node.children.append(temp_child)
        else:
            new_node.children.append(affirm(child, unloaded_components, loaded_components))

    return new_node

def load_component_html(component_info: dict[str, componentInfo]):
    components: dict[str, HtmlElement] = {}
    for ci in component_info:
        cp = component_info[ci]
        if cp.ComponentName not in components:
            loaded_html: str = FileHelpers.load_file(os.path.join(cp.DirPath, f'{cp.ComponentName}.html'))
            components[cp.ComponentName] = parse_html(loaded_html)
    return components

def stitch_project(index_filepath, components_dir):
    comps = get_components(components_dir)
    unloaded_components: dict[HtmlElement] = load_component_html(comps)
    loaded_components: dict[HtmlElement] = {}

    html = FileHelpers.load_file(index_filepath)
    tree: HtmlElement = parse_html(html)

    #rar = stitch_components(tree, unloaded_components, loaded_components)
    rar = affirm(tree, unloaded_components, loaded_components)
    return rar
