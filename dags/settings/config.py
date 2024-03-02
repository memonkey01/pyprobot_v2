import os
from dotenv import load_dotenv
load_dotenv()

ORDER_SIZE_DEFAULT = 10


BYBIT_API_KEY = os.environ['BYBIT_KEY']
BYBIT_API_SECRET = os.environ['BYBIT_SECRET']

CONFIG_MYSQL = {
    'host': 'pypro_db',
    'user': 'pypro',
    'password': 'pypro',
    'db': 'pypro'
}