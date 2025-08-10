from give.context import Context


def unadd(ctx: Context, *file_names: tuple[str]):
    print(f'checkout command: {file_names}')
