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
    

def get_components(path: str) -> set[componentInfo]:
    component_dirs = []
    contents = os.listdir(path)
    for item in contents:
        if os.path.isdir(item) and contains_file(item, "component.json"):
            comp = CreateComponentInfo(item)
            component_dirs.append(comp)
    return component_dirs

def process_node(node: HtmlElement, components: set[componentInfo]) -> None:
    if node.name in components:
        pass

def bfs(node):
    for child in node.children:
        print(child.name)
        bfs(child)

def main():
    comps = get_components(".")
    for comp in comps:
        print(comp.ComponentName)

    parser = JessicaParser.JessicaParser()

    html = FileHelpers.load_file("./templates/index.html")
    parser.feed(html)
    bfs(parser.elements[0])

if __name__ == '__main__':
    #main()
    ComponentCreator.create_component("Jess", ".")