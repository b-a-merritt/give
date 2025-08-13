from collections.abc import Callable
from re import compile

from give.helpers.path import protec_file_path
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
    protec = protec_file_path(root)

    if protec.exists():
        patterns = read(protec)
        
        return [_create_matcher(pattern) for pattern in patterns]
        
    return []