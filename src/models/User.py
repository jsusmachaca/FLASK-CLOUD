from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id, full_name, username, password) -> None:
        self.id = id
        self.full_name = full_name
        self.username = username
        self.password = password

    @classmethod
    def showPassword(cls, passwd_hashed: str, password: str) -> bool:
        return check_password_hash(passwd_hashed, password)
    
    @classmethod
    def id_user(cls, con, id):
        try:
            cur = con.cursor()
            cur.execute('SELECT id, full_name, username FROM users WHERE id=%s;' %id)
            row = cur.fetchone()
            return User(row[0], row[1], row[2], None)
        
        except Exception:
            print('\033[31mOcurrió un Error con la base de datos\033[0m')
