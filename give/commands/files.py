from pathlib import Path

from give.context import Context


def files(ctx: Context) -> list[str]:
    """
    Collects all files not ignored from the give project
    """
    path_queue = [Path(ctx.root)]
    files_: list[str] = []

    while len(path_queue):
        curr = path_queue.pop(0)
        for entry in curr.iterdir():
            entry_str = str(entry)

            for test_ in ctx.ignore_patterns:
                if test_(entry_str):
                    break
            else:
                if entry.is_dir():
                    path_queue.append(entry)
                else:
                    files_.append(str(entry.resolve()))
    
    return files_

def files_cmd(ctx: Context) -> None:
    fs = files(ctx)
    for file in fs:
        print(file)