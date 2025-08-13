from give.helpers.path import current_commit_history_path
from give.helpers.read import read

def current_commit(root: str, branch: str) -> str:
    return read(str(current_commit_history_path(root, branch)))[-1]
