class UserNotFound(Exception):
    def __init__(self):
        super().__init__("User Not Found")