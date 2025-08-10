class NotGiveProject(Exception):
    def __init__(self, message="This is not a give project"):
        super().__init__(message)

    def __str__(self):
        return f"{self.args[0]}"

class AlreadyGiveProject(Exception):
    def __init__(self, message="This project has already been give-initialized"):
        super().__init__(message)

    def __str__(self):
        return f"{self.args[0]}"
    
class CommandNotFound(Exception):
    def __init__(self, message="Give has no such command"):
        super().__init__(message)

    def __str__(self):
        return f"{self.args[0]}"
    