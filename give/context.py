from collections.abc import Callable

from give.constants import GIVE_CMD_INIT
from give.helpers.current_branch import current_branch
from give.helpers.current_commit import current_commit
from give.helpers.ignore import ignore
from give.helpers.where import where

class Context():
    root: str
    ignore_patterns: list[Callable[[str], bool]]
    curr_branch: str
    curr_commit: str

    def __init__(self, cmd: str):
        if cmd == GIVE_CMD_INIT:
            return

        self.root = where()
        self.ignore_patterns = ignore(self.root)
        self.curr_branch = current_branch(self.root)
        self.curr_commit = current_commit(self.root, self.curr_branch)

    def __repr__(self):
        return f"Context(root={self.root}, curr_branch={self.curr_branch}, curr_commit={self.curr_commit})"
