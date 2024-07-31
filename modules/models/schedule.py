from sqlalchemy import Column, Integer, String, Boolean
from .base import Base


class Schedule(Base):
    __tablename__ = 'Schedule'

    id = Column(Integer, primary_key=True)
    week_schedule = Column(Integer)
    weekday = Column(Integer)
    data_lessons = Column(String(512))  # Default data lessons
