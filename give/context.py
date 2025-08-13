from collections.abc import Callable

from give.constants import GIVE_CMD_INIT
from give.helpers.collect_changes import collect_changes
from give.helpers.current_branch import current_branch
from give.helpers.current_commit import current_commit
from give.helpers.ignore import ignore
from give.helpers.path import current_commit_changes_path
from give.helpers.path import staging_path
from give.helpers.where import where

class Context():
    root: str
    ignore_patterns: list[Callable[[str], bool]]
    curr_branch: str
    curr_commit: str
    staging_changes: dict[str, list[str]]
    prev_commit_changes: dict[str, list[str]]

    def __init__(self, cmd: str):
        if cmd == GIVE_CMD_INIT:
            return

        self.root = where()
        self.ignore_patterns = ignore(self.root)
        self.curr_branch = current_branch(self.root)
        self.curr_commit = current_commit(self.root, self.curr_branch)
        self.staging_changes = collect_changes(str(staging_path(self.root)))
        self.prev_commit_changes = collect_changes(str(current_commit_changes_path(self.root, self.curr_commit)))

    def __repr__(self):
        return f"Context(root={self.root}, curr_branch={self.curr_branch}, curr_commit={self.curr_commit})"
