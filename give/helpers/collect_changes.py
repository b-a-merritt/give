from pathlib import Path

from give.helpers.read import read

def collect_changes(dir_name: str) -> dict[str, list[str]]:
    dir_ = Path(dir_name)
    changes = dict()

    for file in dir_.iterdir():
        file_path = str(file)
        file_changes = read(file_path)
        dict[file_path] = file_changes

    return changes