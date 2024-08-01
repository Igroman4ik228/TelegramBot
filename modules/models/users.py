from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    is_notify = Column(Boolean, default=True)
    name = Column(String(124))
    telegram_id = Column(Integer)

    def __str__(self):
        return (f"\nId: {self.id}\nName: {self.name}"
                f"\nIsNotify: {self.is_notify}\nTelegramId: {self.telegram_id}")

