from bs4 import BeautifulSoup
from config import Url, MyGroup
from logging import getLogger
from modules.builder import main_build

import requests

logger = getLogger(__name__)

GROUP_DATA_TEMPLATE = [[i, None] for i in range(7)]


def main_parse():
    """Main function to parse the schedule from a given URL."""
    try:
        response = requests.get(Url)
        response.encoding = 'utf-8'
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('table')

        if data is None:
            raise Exception("Не найдена таблица с расписанием")

        rows = data.find_all('tr')

        rows = rows[1:]  # Skip the first row if it's a header

        group_data = extract_group_data(rows, MyGroup)
        
        logger.info(f"{group_data}")
        
        day_of_week = get_day_of_week(soup)
        week_schedule = get_week_schedule(soup)
        # Build current lesson
        main_build(group_data, day_of_week, week_schedule)

    except Exception as e:
        logger.error(e)
        return


def extract_group_data(rows, target_group):
    """Extract group data from table rows for the target group."""
    group_data = GROUP_DATA_TEMPLATE.copy()

    for row in rows:
        cells = row.find_all('td')
        group = cells[1].text.strip()

        if group == target_group:
            row_data = extract_row_data(cells)
            lesson_numbers = cells[2].text.strip()
            valid_replacement = validate_numbers_replacement_lessons(lesson_numbers)

            for number in valid_replacement:
                group_data[number] = [number, row_data]
    
    return group_data


def extract_row_data(cells):
    """Extract data from a row, handling replacement information."""
    subject = cells[4].text.strip()
    replacement_info = cells[5].text.strip()
    if replacement_info:
        return f"{subject} {replacement_info} (❗ замена)"
    return f"{subject} (❗ замена)"


def validate_numbers_replacement_lessons(numbers_replacement_lessons: str):
    """Validate and parse the replacement lesson numbers."""
    valid_nums_list = []

    if ',' in numbers_replacement_lessons:
        splited_numbers = numbers_replacement_lessons.split(',')
        for number in splited_numbers:
            valid_nums_list.append(int(number))
    elif '-' in numbers_replacement_lessons:
        splited_numbers = numbers_replacement_lessons.split('-')
        start = int(splited_numbers[0])
        end = int(splited_numbers[-1])
        valid_nums_list.extend(range(start, end + 1))
    elif '.' in numbers_replacement_lessons:
        splited_number = float(numbers_replacement_lessons)
        valid_nums_list = get_lesson_number_by_time(splited_number)
    elif len(numbers_replacement_lessons) == 1:
        valid_nums_list.append(int(numbers_replacement_lessons))
    else:
        raise Exception(f"Неправильный формат номера замены: {numbers_replacement_lessons}")

    return valid_nums_list


# todo: Больше промежутков
def get_lesson_number_by_time(time_float):
    """Determine the lesson number based on time."""
    if time_float <= 9.10:
        return [0]
    elif time_float <= 10.50:
        return [1]
    elif time_float <= 12.30:
        return [2]
    elif time_float <= 14.50:
        return [3]
    elif time_float <= 16.35:
        return [4]
    elif time_float <= 18.35:
        return [5]
    else:
        return [6]


def get_day_of_week(soup):
    """Extract the day of the week from the soup object."""
    data = soup.find_all('div')
    full_day_of_week = data[2].get_text()
    return str.split(full_day_of_week, ' ')[-1]


def get_week_schedule(soup):
    data = soup.find_all('div')
    full_day_of_week = data[3].get_text()
    result = str.split(full_day_of_week, ' ')[0]
    # 1 - числитель 2 - знаменатель
    if result == "(Числитель)": 
        return 1
    elif result == "(Знаменатель)":
        return 2
    raise Exception(f"Не удалось определить числитель/знаменатель: {result}")
