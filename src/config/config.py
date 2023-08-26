from decouple import config



class Config:
    def __init__(self) -> None:
        self.DEBUG = True if config('DEBUG') == 'true' else False
        self.MYSQL_HOST = config('DB_HOST')
        self.MYSQL_DB = config('DB_NAME')
        self.MYSQL_USER = config('DB_USER')
        self.MYSQL_PASSWORD = config('DB_PASSWORD')
        self.SESSION_PERMANENT = True if config('SESSION_PERMANENT') == 'true' else False
        self.SESSION_TYPE = config('SESSION_TYPE')
