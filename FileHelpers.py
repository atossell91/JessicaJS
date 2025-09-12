import os

def load_file(path: str) -> str:
    with open(path, 'r') as file:
        text = file.read(-1)
        return text
    
def write_file(content: str, path: str) -> None:
    with open(path, 'w') as file:
        file.write(content)

def create_file(name: str, directory: str, source_path: str, extension) -> None:
    file_name = f'{name}.{extension}'
    file_path = os.path.join(directory, file_name)
    content = load_file(source_path)
    write_file(content, file_path)