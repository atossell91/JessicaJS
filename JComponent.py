import os
from dataclasses import dataclass
import json

from FileHelpers import load_file
from Utils import expand_path

@dataclass
class Component:
    ComponentName: str
    ComponentDirpath: str
    HtmlPath: str
    ManifesrPath: str
    HtmlTag: str
    ManifestData: dict[str, str]

    JavascriptPath: str = None
    CssPath: str = None
    HtmlText: str = None

    def __post_init__(self):
        self.HtmlTag = self.HtmlTag.lower()

    def GetHtmlText(self):
        if self.HtmlText is None and not os.path.exists(self.HtmlPath):
            return None
        
        if self.HtmlText is None:
            self.HtmlText = load_file(self.HtmlPath)

        return self.HtmlText
    
def is_component(directory):
    return  "component.json" in os.listdir(directory)
    
def load_component(component_dirpath):
    root_path = expand_path(component_dirpath)

    manifest_path = os.path.join(root_path, "component.json")
    manifest_data = None
    with open(manifest_path, 'r') as manifest:
        manifest_data = json.load(manifest)
    
    dir_name = os.path.split(root_path)[1]
    comp_name = manifest_data["name"]

    tag = comp_name
    if "tag" in manifest_data:
        tag = manifest_data["tag"]
    tag = tag.lower()

    js_path = os.path.join(root_path, f'{comp_name}.js')
    if not os.path.exists(js_path):
        js_path = None

    css_path = os.path.join(root_path, f'{comp_name}.css')
    if not os.path.exists(css_path):
        css_path = None

    component: Component = Component(
        ComponentName=comp_name,
        ComponentDirpath=root_path,
        HtmlPath=os.path.join(root_path, f"{comp_name}.html"),
        ManifesrPath=manifest_path,
        HtmlTag=tag,
        ManifestData=manifest_data,
        CssPath=css_path,
        JavascriptPath=js_path
    )

    return component
