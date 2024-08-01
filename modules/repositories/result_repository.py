from modules.models.result import ResultSchedule


class ResultRepository:
    def __init__(self, session):
        self.session = session

    def create(self, weekday, data_lessons):
        new_schedule = ResultSchedule(
            weekday=weekday,
            final_lesson=data_lessons
        )
        self.session.add(new_schedule)
        self.session.commit()

    def get(self, weekday):
        return (self.session.query(ResultSchedule)
                .filter_by(weekday=weekday)
                .first())

    def delete(self, weekday):
        schedule = self.get(weekday)
        if schedule:
            self.session.delete(schedule)
            self.session.commit()
        else:
            raise ValueError(f"Schedule with "
                             f"weekday={weekday} does not exist.")
