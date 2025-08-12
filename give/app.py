from collections.abc import Callable

from give.context import Context
from give.exceptions import CommandNotFound

class Give():
    commands: dict[str, Callable] = dict()
    ctx: Context

    def register(self, name: str, cmd: Callable[[Context], None]):
        self.commands[name] = cmd

    def run(self, name: str, *args: tuple[str]):
        cmd = self.commands.get(name)

        if not cmd:
            raise CommandNotFound()
        
        self.ctx = Context(name)
        cmd(self.ctx, *args)
