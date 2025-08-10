from pathlib import Path

from give.constants import GIVE_DIR
from give.exceptions import NotGiveProject


def where() -> str:
    """
    Returns the absolute path of the nearest parent .give directory
    """
    curr = Path('.').resolve()
    root = Path('/').resolve()

    while True:
        give = Path(f'{curr}/{GIVE_DIR}')

        if give.exists():
            return str(curr)

        if root == curr:
            raise NotGiveProject()

        curr = curr.parents[0]
