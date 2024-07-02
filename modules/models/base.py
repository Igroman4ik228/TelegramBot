import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv, find_dotenv
import os

# Загрузка переменных окружения
load_dotenv(find_dotenv())

Base = declarative_base()


def get_engine():
    engine = db.create_engine(f"{os.getenv('SQL_Connection')}")
    return engine
