from give.constants import GIVE_CURRENT_BRANCH
from give.constants import GIVE_DIR
from give.helpers.read import read

def current_branch(root: str) -> str:
    return read(f'{root}/{GIVE_DIR}/{GIVE_CURRENT_BRANCH}')[0]
