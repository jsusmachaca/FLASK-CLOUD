from decouple import config



class DevConfig:
    def __init__(self) -> None:
        self.DEBUG = True if config('DEBUG') == 'true' else False
        self.SECRET_KEY = 'acdgjDFsusafsHd__asd'
        self.SESSION_TYPE = 'filesystem'

class Path:
    dir_path = None