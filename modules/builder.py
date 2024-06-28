import json
from datetime import datetime
from logging import getLogger
logger = getLogger(__name__)


class ScheduleBuilder:
    def __init__(self):
        self._localAPI = LocalAPI()

    def main_build(self):
        week_of_schedule = 1

        default_lesson = self._localAPI.get_default_schedule(week_of_schedule, datetime.today().weekday())
        replacement_lesson = self._localAPI.get_replacement_lesson(datetime.today().weekday())

        default_data = json.loads(default_lesson.serialize_data_lessons)
        replace_data = None

        if replacement_lesson:
            replace_data = json.loads(replacement_lesson.serialize_data_lessons)

        current_schedule = self.build_current_schedule(replace_data, default_data)
        self.write_to_database(current_schedule)
        logger.info("Current schedule was loaded into database")

    @staticmethod
    def build_current_schedule(replace_data, default_data):
        if replace_data:
            for key in default_data:
                if key in replace_data and replace_data[key]:
                    default_data[key] = replace_data[key]
        return json.dumps(default_data, indent=4)\


    def write_to_database(current_data):
        logger.debug(f"\n{current_data}")


builder = ScheduleBuilder()
builder.main_build()