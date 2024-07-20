class UserAlreadyExistError(ValueError):
    def __init__(self, message="User already exists."):
        super().__init__(message)
