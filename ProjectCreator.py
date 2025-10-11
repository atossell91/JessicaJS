import os

import Utils
from FileHelpers import create_file

root = Utils.get_jessica_root()
template_dir = os.path.join(root, "templates")

index_file = os.path.join(template_dir, "index.html")

def create_project(name: str) -> None:
    # Create the index file
    create_file("index", ".", index_file, "html")
