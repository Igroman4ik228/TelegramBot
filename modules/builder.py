from logging import getLogger

logger = getLogger(__name__)


def main_build(replace_lesson, day_of_week, week_schedule):
    default_lesson = [
            [0, "Психология общения Сурова Ю.В. - Б501"],
            [1, "МДК 02.02 Инструментальные средства разработки ПО Пронина Л.Ю. - Б504"],
            [2, "МДК 08.01 Проектирование и разработка интерфейсов пользователя Гудкова А.Л., Вакансия - Б301, Б305"],
            [3, None],
            [4, None],
            [5, None],
            [6, None]
    ] # Из бд
    
    current_lesson = build_current_schedule(default_lesson, replace_lesson)
    beautiful_lesson = create_beautiful_lesson(current_lesson, day_of_week, week_schedule)
    write_to_database(beautiful_lesson, day_of_week, week_schedule)
    
    
def build_current_schedule(default_lesson, replace_lesson):
    if default_lesson:
        for i in range(0, len(default_lesson)):
            if replace_lesson[i][1] != None:
                default_lesson[i][1] = replace_lesson[i][1]
    return default_lesson


def create_beautiful_lesson(current_lesson, day_of_week, week_schedule):
    if week_schedule == 1:
        week_schedule == "Числитель"
    elif week_schedule == 2:
        week_schedule == "Знаменатель"
    
    beautiful_lesson = f"Расписание на {day_of_week} ({week_schedule}): \n"
    for lesson in current_lesson:
        if lesson[1]!= None:
            beautiful_lesson += f"`{lesson[0]}.` **{lesson[1]}**\n"
    return beautiful_lesson


def write_to_database(final_lesson, day_of_week, week_schedule):
    logger.info(f"Записываем расписание в базу данных на {day_of_week} {week_schedule}:\n {final_lesson}")