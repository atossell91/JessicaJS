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

    ##  Unpack the component and set it to the new node
    if current_element.name in components:
        new_node = recursive_stitch(components[current_element.name], components)
    ##  Set the new node to the existing node
    else:
        ## Create a new HTML Element
        new_node: HtmlElement = HtmlElement(current_element.name)
        new_node.data = current_element.data
        new_node.attributes = current_element.attributes

    for child in current_element.children:
        temp_node = recursive_stitch(child, components)
        
        ##  If the node is root, only append it's children
        if temp_node.name == 'root':
            for temp_child in temp_node.children:
                new_node.children.append(temp_child)

        ##  Otherwise append it, as-is
        else:
            new_node.children.append(recursive_stitch(child, components))

    return new_node

def find_components(directory) -> dict[str, Component]:
    items = os.listdir(directory)
    comps: dict[str, Component] = {}
    for item in items:
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and is_component(item_path):
            comp = load_component(item_path)
            comps[comp.ComponentName] = comp
    return comps

def stich_component(component: Component) -> HtmlElement:
    components = find_components(component.ComponentDirpath)
    component_trees: dict[str, HtmlElement] = {}

    for component_name in components:
        child_comp = components[component_name]
        child_tree = stich_component(child_comp)
        component_trees[child_comp.HtmlTag] = child_tree
        
    index_tree = parse_html(component.GetHtmlText())
    return recursive_stitch(index_tree, component_trees)
