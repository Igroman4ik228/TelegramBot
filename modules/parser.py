from bs4 import BeautifulSoup
from config import Url, MyGroup
from logging import getLogger
from modules.builder import main_build

import requests

logger = getLogger(__name__)

def main_parse():
    response = requests.get(Url)
    response.encoding = 'utf-8'

    try:
        if response.status_code == 200:

            soup = BeautifulSoup(response.text, 'lxml')
            
            data = soup.find('table')

            if data is None:
                raise Exception("Не найдена таблица с расписанием")

            rows = data.find_all('tr')

            if rows:
                rows = rows[1:]  # Skip the first row if it's a header
            else:
                raise Exception("Не найдены строки в таблице")

            group_data = [
                [0, None],
                [1, None],
                [2, None],
                [3, None],
                [4, None],
                [5, None],
                [6, None]
            ]

            for row in rows:
                cells = row.find_all('td')
                group = cells[1].text.strip()

                if group != "" and group != " " and group != "\n" and group == MyGroup:
                    if cells[5].text.strip() != "":
                        row_data = f"{cells[4].text.strip()} {cells[5].text.strip()} (❗ замена)"
                    else:
                        row_data = f"{cells[4].text.strip()} (❗ замена)"

                    numbers_replacement_lessons = cells[2].text.strip()
                    valid_replacement = validate_numbers_replacement_lessons(numbers_replacement_lessons)
                    for number in valid_replacement:
                        group_data[number] = [number, row_data]
            
            logger.info(f"{group_data}")
            
            day_of_week = get_day_of_week(soup)
            # Build current lesson
            main_build(group_data, day_of_week)
            
        else:
            raise Exception(f"Ошибка сети: {response.status_code}")

    except Exception as e:
        logger.error(e)
        return


def validate_numbers_replacement_lessons(numbers_replacement_lessons: str):
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
        if splited_number <= 9.10:
            valid_nums_list.append(0)
        elif splited_number <= 10.50:
            valid_nums_list.append(1)
        elif splited_number <= 12.30:
            valid_nums_list.append(2)
        elif splited_number <= 14.50:
            valid_nums_list.append(3)
        elif splited_number <= 16.35:
            valid_nums_list.append(4)
        elif splited_number <= 18.35:
            valid_nums_list.append(5)
        else:
            valid_nums_list.append(6)
    elif len(numbers_replacement_lessons) == 1:
        valid_nums_list.append(int(numbers_replacement_lessons))
    else:
        raise Exception(f"Неправильный формат номера замены: {numbers_replacement_lessons}")

    return valid_nums_list



def get_day_of_week(soup):
    data = soup.find_all('div')
    full_day_of_week = data[2].get_text()
    return str.split(full_day_of_week, ' ')[-1]
