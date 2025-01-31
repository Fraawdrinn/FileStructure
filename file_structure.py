"""."""
import os
from pathlib import Path

elements = []
white_list = ["node_modules"]
exclude_extensions = [".svg", ".ico", ".json", ".png", ".jpg"]

def list_element(dir: Path, children: list, before: str = "", dir_count: int = 0):
    before += "  " * dir_count
    dir_count += 1
    for child in dir.iterdir():
        if child.name[0] == "." or child.name in white_list:
            children.append(before + str(child.relative_to(dir)) + "\n")
        elif child.is_dir():
            children.append(before + str(child.relative_to(dir)) + "/\n")
            list_element(child, children, before, dir_count)
        elif child.suffix not in exclude_extensions:
            children.append(before + str(child.relative_to(dir)) + "\n")
    return children

def write_element(liste: list, output_file: str = "directory_children.txt"):
    with Path(output_file).open("w") as file:
        file.writelines(liste)

# Example usage:
# directory_path = Path(input("Enter the directory path: "))
directory_path = Path("C:/Users/chato/PROJETS/blog")
list_element(directory_path, elements)
write_element(elements)
