from modules.models.schedule import Schedule


class ScheduleRepository:
    """
    Example of work with Repository

    _repository = ScheduleRepository(session)
    _repository.create(1, 1, "Programming")
    """

    def __init__(self, session):
        self.session = session

    def create(self, week_schedule, weekday, data_lessons):
        new_schedule = Schedule(
            week_schedule=week_schedule,
            weekday=weekday,
            data_lessons=data_lessons)
        self.session.add(new_schedule)
        self.session.commit()

    def get(self, week_schedule, weekday):
        return (self.session.query(Schedule)
                .filter_by(week_schedule=week_schedule,
                           weekday=weekday)
                .first())
