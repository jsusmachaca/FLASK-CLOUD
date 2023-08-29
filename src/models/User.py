from werkzeug.security import check_password_hash

class User:
    def __init__(self, id, full_name, username, password) -> None:
        self.id = id
        self.full_name = full_name
        self.username = username
        self.password = password

    @classmethod
    def showPassword(cls, passwd_hashed: str, password: str) -> bool:
        return check_password_hash(passwd_hashed, password)