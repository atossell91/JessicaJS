import ProjectCreator
import ComponentCreator

import FileHelpers
import JessicaParser

import html.parser
import re
import os
def contains_file(directory, filename):
    return os.path.isfile(os.path.join(directory, filename))

def replace(content, tag_name, body):
    full_tag = f'<{tag_name}/>'


def get_components(path: str):
    component_dirs = []
    contents = os.listdir(path)
    for item in contents:
        if os.path.isdir(item) and contains_file(item, "component.json"):
            component_dirs.append(item)
    return component_dirs

def bfs(node):
    for child in node.children:
        print(child.name)
        bfs(child)

def main():
    parser = JessicaParser.JessicaParser()

    html = FileHelpers.load_file("./templates/index.html")
    parser.feed(html)
    bfs(parser.elements[0])

if __name__ == '__main__':
    main()