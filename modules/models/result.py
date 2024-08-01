from sqlalchemy import Column, Integer, String
from .base import Base


class ResultSchedule(Base):
    __tablename__ = 'ResultSchedule'

    id = Column(Integer, primary_key=True)
    weekday = Column(Integer)
    final_lesson = Column(String(1024))

    def __str__(self):
        return (f"\nId: {self.id}"
                f"\nWeekday: {self.weekday}\nData: {self.final_lesson}")
