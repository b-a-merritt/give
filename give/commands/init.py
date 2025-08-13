import os

from give.context import Context
from give.constants import GIVE_AFTER
from give.constants import GIVE_BEFORE
from give.constants import GIVE_BRANCH_HISTORY
from give.constants import GIVE_BRANCHES_DIR
from give.constants import GIVE_COMMITS_DIR
from give.constants import GIVE_CURRENT_BRANCH
from give.constants import GIVE_DEFAULT_BRANCH
from give.constants import GIVE_DIR
from give.constants import GIVE_INITIAL_COMMIT
from give.constants import GIVE_STAGING_DIR
from give.exceptions import AlreadyGiveProject

def init(_: Context) -> None:
    """
    Initializes a give project
    """
    if os.path.isdir(GIVE_DIR):
        raise AlreadyGiveProject()

    # globals
    os.mkdir(GIVE_DIR)
    branch = open(f'{GIVE_DIR}/{GIVE_CURRENT_BRANCH}', 'w')
    branch.write(GIVE_DEFAULT_BRANCH)

    # branch directories
    os.mkdir(f'{GIVE_DIR}/{GIVE_BRANCHES_DIR}')
    os.mkdir(f'{GIVE_DIR}/{GIVE_BRANCHES_DIR}/{GIVE_DEFAULT_BRANCH}')
    
    branch_history = open(f'{GIVE_DIR}/{GIVE_BRANCHES_DIR}/{GIVE_DEFAULT_BRANCH}/{GIVE_BRANCH_HISTORY}', 'w')
    branch_history.write(GIVE_INITIAL_COMMIT)

    # commit directories
    os.mkdir(f'{GIVE_DIR}/{GIVE_COMMITS_DIR}')
    os.mkdir(f'{GIVE_DIR}/{GIVE_COMMITS_DIR}/{GIVE_INITIAL_COMMIT}')
    os.mkdir(f'{GIVE_DIR}/{GIVE_COMMITS_DIR}/{GIVE_INITIAL_COMMIT}/{GIVE_BEFORE}')
    os.mkdir(f'{GIVE_DIR}/{GIVE_COMMITS_DIR}/{GIVE_INITIAL_COMMIT}/{GIVE_AFTER}')

    # stage
    os.mkdir(f'{GIVE_DIR}/{GIVE_STAGING_DIR}')
