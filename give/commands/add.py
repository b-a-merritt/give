from pathlib import Path

from give.context import Context
from give.exceptions import InsufficientParameters
from give.helpers.hash import hash_file
from give.helpers.list_files import list_files


def add(ctx: Context, *paths: tuple[str]):
    if not paths:
        raise InsufficientParameters()
    
    for path in paths:
        files = list_files(path, ctx.ignore_patterns)
        print(files)