class GeneralException(Exception):
    def __str__(self):
        return f"{self.args[0]}"

class NotGiveProject(GeneralException):
    def __init__(self, message="This is not a give project"):
        super().__init__(message)

class AlreadyGiveProject(GeneralException):
    def __init__(self, message="This project has already been give-initialized"):
        super().__init__(message)
    
class CommandNotFound(GeneralException):
    def __init__(self, message="Give has no such command"):
        super().__init__(message)

class InsufficientParameters(GeneralException):
    def __init__(self, message="Insufficient number of parameters"):
        super().__init__(message)