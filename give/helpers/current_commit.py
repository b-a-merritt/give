from give.constants import GIVE_BRANCHES_DIR
from give.constants import GIVE_DIR
from give.constants import GIVE_BRANCH_HISTORY
from give.helpers.read import read

def current_commit(root: str, branch: str) -> str:
    return read(f'{root}/{GIVE_DIR}/{GIVE_BRANCHES_DIR}/{branch}/{GIVE_BRANCH_HISTORY}')[-1]
