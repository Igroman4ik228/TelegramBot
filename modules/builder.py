from logging import getLogger

logger = getLogger(__name__)

def main_build():
    defaultLesson = [
            [0, "Психология общения Сурова Ю.В. - Б501"],
            [1, "МДК 02.02 Инструментальные средства разработки ПО Пронина Л.Ю. - Б504"],
            [2, "МДК 08.01 Проектирование и разработка интерфейсов пользователя Гудкова А.Л., Вакансия - Б301, Б305"],
            [3, None],
            [4, None],
            [5, None],
            [6, None]
    ]
    
    replaceLesson = [
            [0, None],
            [1, None],
            [2, None],
            [3, None],
            [4, None],
            [5, None],
            [6, "Психология общения Сурова Ю.В. - Б501"]
    ]
    
    currentLesson = build_current_schedule(defaultLesson, replaceLesson)
    logger.info(f"Текущее расписание: {currentLesson}")
    
    
def build_current_schedule(defaultLesson, replaceLesson):
    if defaultLesson:
        for i in range(0, len(defaultLesson)):
            if replaceLesson[i][1] != None:
                defaultLesson[i][1] = replaceLesson[i][1]
    return defaultLesson


main_build()