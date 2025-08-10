from give.context import Context


def checkout(ctx: Context, branch_name: str):
    print(f'checkout command: {branch_name}')
