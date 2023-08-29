from pymysql import connect
from decouple import config

def con():
    return connect(
        host=config('DB_HOST'),
        database=config('DB_NAME'),
        user=config('DB_USER'),
        passwd=config('DB_PASSWORD')
    )