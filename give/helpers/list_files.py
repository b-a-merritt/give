from collections.abc import Callable
from pathlib import Path


def list_files(path: str, ignore_patterns: list[Callable[[str], bool]]) -> list[str]:
    """
    Collects all files not ignored from the give project
    """
    path_queue = []
    files: list[str] = []

    if any(test(path) for test in ignore_patterns):
        return []
    
    curr = Path(path)
    if curr.is_dir():
        path_queue.append(curr)
    else:
        files.append(str(curr.resolve()))

    while len(path_queue):
        curr = path_queue.pop(0)
        for entry in curr.iterdir():
            entry_str = str(entry)

            if any(test_(entry_str) for test_ in ignore_patterns):
                continue
            else:
                if entry.is_dir():
                    path_queue.append(entry)
                else:
                    files.append(str(entry.resolve()))

    return files
