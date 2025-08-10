from give.context import Context


def add(ctx: Context, *file_names: tuple[str]):
    print(f'add command: {file_names}')
