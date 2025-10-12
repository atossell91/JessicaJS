import os
import json

import FileHelpers

from ComponentInfo import componentInfo
from HtmlElement import HtmlElement
from JessicaParser import parse_html

from JComponent import Component
from JComponent import is_component
from JComponent import load_component

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
    loaded_components: dict[str, HtmlElement] = {}

    html = FileHelpers.load_file(index_filepath)
    tree: HtmlElement = parse_html(html)

    #rar = stitch_components(tree, unloaded_components, loaded_components)
    rar = affirm(tree, unloaded_components, loaded_components)
    return rar
