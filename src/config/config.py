from decouple import config


class Config:
    def __init__(self) -> None:
        self.SECRET_KEY = 'acdgjDFsusafsHd__asd'

class DevConfig(Config):
    def __init__(self) -> None:
        super().__init__()
        self.DEBUG = True if config('DEBUG') == 'true' else False


class Path:
    dir_path = None