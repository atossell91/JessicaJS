import os
import json

import FileHelpers

from ComponentInfo import componentInfo
from HtmlElement import HtmlElement
from JessicaParser import parse_html

from JComponent import Component
from JComponent import is_component
from JComponent import load_component

def recursive_stitch(current_element: HtmlElement,
        components: dict[str, HtmlElement]):

    if current_element.name in components:
        new_node = recursive_stitch(components[current_element.name], components)
    else:
        new_node: HtmlElement = HtmlElement(current_element.name)
        new_node.data = current_element.data
        new_node.attributes = current_element.attributes

    for child in current_element.children:
        temp_node = recursive_stitch(child, components)
        if temp_node.name == 'root':
            for temp_child in temp_node.children:
                new_node.children.append(temp_child)
        else:
            new_node.children.append(recursive_stitch(child, components))

    return new_node

def load_component_html(component_dict: dict[str, Component]):
    components: dict[str, HtmlElement] = {}
    for key in component_dict:
        comp = component_dict[key]
        if comp.ComponentName not in components:
            loaded_html: str = comp.GetHtmlText()
            components[comp.HtmlTag] = parse_html(loaded_html)
    return components

def find_components(directory) -> dict[str, Component]:
    items = os.listdir(directory)
    comps: dict[str, Component] = {}
    for item in items:
        if os.path.isdir(item) and is_component(item):
            comp = load_component(item)
            comps[comp.ComponentName] = comp
    return comps

def stitch_project(index_filepath, components_dir):
    comps = find_components(components_dir)
    unloaded_components: dict[str, HtmlElement] = load_component_html(comps)

    html = FileHelpers.load_file(index_filepath)
    tree: HtmlElement = parse_html(html)

    #rar = stitch_components(tree, unloaded_components, loaded_components)
    rar = recursive_stitch(tree, unloaded_components)
    return rar

def stich_component(component: Component) -> HtmlElement:
    components = find_components(component.ComponentDirpath)
    component_trees: dict[str, HtmlElement] = {}

    for component_name in components:
        child_comp = components[component_name]
        child_tree = stich_component(child_comp.ComponentDirpath)
        component_trees[child_comp.HtmlTag] = child_tree
    
    index_tree = parse_html(component.GetHtmlText())
    return recursive_stitch(index_tree, component_trees)
