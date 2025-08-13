from pathlib import Path

from give.constants import GIVE_BEFORE
from give.constants import GIVE_BRANCHES_DIR
from give.constants import GIVE_BRANCH_HISTORY
from give.constants import GIVE_COMMITS_DIR
from give.constants import GIVE_CURRENT_BRANCH
from give.constants import GIVE_DIR
from give.constants import GIVE_PROTEC
from give.constants import GIVE_STAGING_DIR


def current_branch_path(root: str) -> Path:
    return Path(f'{root}/{GIVE_DIR}/{GIVE_CURRENT_BRANCH}')


def current_commit_changes_path(root: str, commit_name: str) -> Path:
    return Path(f'{root}/{GIVE_DIR}/{GIVE_COMMITS_DIR}/{commit_name}/{GIVE_BEFORE}')


def current_commit_history_path(root: str, branch: str) -> Path:
    return Path(f'{root}/{GIVE_DIR}/{GIVE_BRANCHES_DIR}/{branch}/{GIVE_BRANCH_HISTORY}')


def protec_file_path(root: str) -> Path:
    return Path(f'{root}/{GIVE_PROTEC}')


def staging_path(root: str) -> Path:
    return Path(f'{root}/{GIVE_DIR}/{GIVE_STAGING_DIR}').resolve()