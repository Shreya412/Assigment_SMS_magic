class InvalidEmail(Exception):
    def __init__(self, message="Invalid Email"):
        super(InvalidEmail, self).__init__(message)

class InvalidMessage(Exception):
    def __init__(self, message="Invalid Message"):
        super(InvalidMessage, self).__init__(message)

class InvalidPhoneNumber(Exception):
    def __init__(self, message="Invalid Phone Number"):
        super(InvalidPhoneNumber, self).__init__(message)

class InvalidHours(Exception):
    def __init__(self, message="Invalid hours"):
        super(InvalidHours, self).__init__(message)

class DuplicateMessage(Exception):
    def __init__(self, message="Duplicate Message Found") -> None:
        super(DuplicateMessage, self).__init__(message)