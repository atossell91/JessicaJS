import os
import re

def load_file(path: str) -> str:
    with open(path, 'r') as file:
        text = file.read(-1)
        return text
    
def write_file(content: str, path: str) -> None:
    with open(path, 'w') as file:
        file.write(content)

def find_tags(content: str) -> set[str]:
    tags = set()
    matches = re.findall(r'@[A-z0-9_-]+', content)
    for match in matches:
        tags.add(match[1:])
    return tags

def replace_matching_tags(content: str, template_tags: set[str], replace_data: dict[str, str]) -> str:
    temp_content: str = content
    for provided_tag in replace_data:
        if provided_tag in template_tags:
            temp_content = temp_content.replace(f'@{provided_tag}', replace_data[provided_tag])
    return temp_content

def create_file(name: str, directory: str, source_path: str, extension, data: dict[str, str] = None) -> None:
    file_name = f'{name}.{extension}'
    file_path = os.path.join(directory, file_name)
    content = load_file(source_path)

    if data is not None:
        template_tags: set[str] = find_tags(content)
        content = replace_matching_tags(content, template_tags, data)

    write_file(content, file_path)