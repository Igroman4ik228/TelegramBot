from sqlalchemy.orm import sessionmaker
from modules.models.base import Base, get_engine

# Создание движка базы данных
engine = get_engine()

# Создание фабрики сессий и сессии
Session = sessionmaker(bind=engine)
session = Session()


def create_tables():
    from modules.models.schedule import Schedule
    from modules.models.users import User
    from modules.models.result import ResultSchedule
    Base.metadata.create_all(engine)


# Создание таблиц при необходимости
create_tables()
