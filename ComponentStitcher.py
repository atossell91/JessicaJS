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
        comp = components[current_element.name]
        new_node = recursive_stitch(comp, components)
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
            new_node.children.extend(temp_node.children)
        ##  Otherwise append it, as-is
        else:
            #new_node.children.append(recursive_stitch(child, components))
            new_node.children.append(temp_node)

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

    temp_dict = {}

    # Stitch all of the sub-components
    for component_name in components:
        child_comp = components[component_name]
        child_tree, sub_components = stich_component(child_comp)

        ## Add the components to a temporary dictionary
        for sub_comp in sub_components:
            temp_dict[sub_comp] = sub_components[sub_comp]

        component_trees[child_comp.HtmlTag] = child_tree
    
    ## Merge the temporary dictionary with the current one
    for key in temp_dict:   
        components[key] = temp_dict[key]
        
    # Parse and stitch the current component
    index_tree = parse_html(component.GetHtmlText())
    final_tree = recursive_stitch(index_tree, component_trees)

    return final_tree, components
