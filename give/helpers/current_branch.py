from give.helpers.read import read
from give.helpers.path import current_branch_path

def current_branch(root: str) -> str:
    return read(str(current_branch_path(root)))[0]
