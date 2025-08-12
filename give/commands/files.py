from give.context import Context
from give.helpers.list_files import list_files


def files(ctx: Context) -> None:
    fs = list_files(ctx.root, ctx.ignore_patterns)
    for file in fs:
        print(file)