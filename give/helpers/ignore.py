from collections.abc import Callable
from pathlib import Path
from re import compile

from give.constants import GIVE_PROTEC
from give.helpers.read import read

def _create_matcher(pattern: str) -> Callable[[str], bool]:
    """
    Creates a closure with the compiled regex pattern
    """
    compiled = compile(pattern)
    def matcher (s: str) -> bool:
        return bool(compiled.search(s))
    return matcher

def ignore(root: str) -> list[Callable[[str], bool]]:
    """
    Collects the ignore patterns from .giveprotect
    """
    protec = Path(f'{root}/{GIVE_PROTEC}')

    if protec.exists():
        patterns = read(protec)
        
        return [_create_matcher(pattern) for pattern in patterns]
        
    return []