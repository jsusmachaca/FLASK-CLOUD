from werkzeug.security import check_password_hash, generate_password_hash

class User:
    def __init__(self, id, username, password, full_name=None) -> None:
        self.id = id
        self.full_name = full_name
        self.username = username
        self.password = password

    @classmethod
    def showPassword(cls, passwd_hashed: str, password: str) -> bool:
        return check_password_hash(passwd_hashed, password)
    
    @classmethod
    def generatePassword(cls, password: str) -> str:
        return generate_password_hash(password)