from modules.models.schedule import Schedule


class ScheduleRepository:
    """
    Example of work with Repository

    _repository = ScheduleRepository(session)
    _repository.create(1, 1, "Programming")
    """
    def __init__(self, session):
        self.session = session

    def create(self, week_schedule, weekday, data_lessons, is_replacement=False):
        # Пример использования сессии для добавления данных
        new_schedule = Schedule(is_replacement=is_replacement,
                                week_schedule=week_schedule,
                                weekday=weekday,
                                data_lessons=data_lessons)
        self.session.add(new_schedule)
        self.session.commit()
