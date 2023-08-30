import pymysql
from decouple import config

def con():
    try:
        return pymysql.connect(
            host=config('DB_HOST'),
            database=config('DB_NAME'),
            user=config('DB_USER'),
            passwd=config('DB_PASSWORD')
        )

    except pymysql.OperationalError:
        print('\033[31mOcurrió un error con la base de datos\033[0m')

    except ConnectionRefusedError:
        print('\033[31mNo se pudo conectar a la base de datos\033[0m')

    except Exception:
        print('\033[31mNo se pudo conectar a la base de datos\033[0m')