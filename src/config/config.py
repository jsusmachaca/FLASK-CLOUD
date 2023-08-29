from decouple import config



class DevConfig:
    def __init__(self) -> None:
        self.DEBUG = True if config('DEBUG') == 'true' else False
        self.SESSION_PERMANENT = True if config('SESSION_PERMANENT') == 'true' else False
        self.SESSION_TYPE = config('SESSION_TYPE')

class Path:
    dir_path = None