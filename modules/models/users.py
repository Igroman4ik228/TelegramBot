from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    is_admin = Column(Boolean, default=False)
    name = Column(String(124))
    telegram_id = Column(Integer)
    # ToDo notification_status: true - получать пуш уведомления при обновлении расписания, False - не получать
