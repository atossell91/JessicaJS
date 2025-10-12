import os
from dataclasses import dataclass
import json

from FileHelpers import load_file

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
    dir_name = os.path.split(component_dirpath)[1]

    manifest_path = os.path.join(component_dirpath, "component.json")
    manifest_data = None
    with open(manifest_path, 'r') as manifest:
        manifest_data = json.load(manifest)

    tag = dir_name
    if "tag" in manifest_data:
        tag = manifest_data["tag"]
    tag = tag.lower()

    js_path = os.path.join(component_dirpath, f'{dir_name}.js')
    if not os.path.exists(js_path):
        js_path = None

    css_path = os.path.join(component_dirpath, f'{dir_name}.css')
    if not os.path.exists(css_path):
        css_path = None

    component: Component = Component(
        ComponentName=dir_name,
        ComponentDirpath=component_dirpath,
        HtmlPath=os.path.join(component_dirpath, f"{dir_name}.html"),
        ManifesrPath=manifest_path,
        HtmlTag=tag,
        ManifestData=manifest_data,
        CssPath=css_path,
        JavascriptPath=js_path
    )

    return component
