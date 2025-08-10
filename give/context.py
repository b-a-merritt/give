from give.helpers.current_branch import current_branch
from give.helpers.ignore import ignore
from give.helpers.where import where

class Context():
    root: str
    ignore_patterns: list[str]
    curr_branch: str
    curr_commit: str

    def __init__(self):
        self.root = where()
        self.ignore_patterns = ignore(self.root)
        self.curr_branch = current_branch('.')
