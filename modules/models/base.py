import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv, find_dotenv
import os

# Загрузка переменных окружения
load_dotenv(find_dotenv())

Base = declarative_base()


def get_engine():
    is_debug = os.getenv('ISDEBUG')
    
    sql_connection = os.getenv('SQL_CONNECTION_DEBUG') if is_debug else os.getenv('SQL_CONNECTION_RELEAS')
    
    engine = db.create_engine(sql_connection)

    return engine
