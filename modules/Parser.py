import requests
from bs4 import BeautifulSoup
from config import Url, MyGroup


def main():
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
                [0, ""],
                [1, ""],
                [2, ""],
                [3, ""],
                [4, ""],
                [5, ""],
                [6, ""]
            ]

            for row in rows:
                cells = row.find_all('td')
                group = cells[1].text.strip()

                if group != "" and group != " " and group != "\n" and group == MyGroup:

                    numbers_replacement_lessons = cells[2].text.strip()
                    valid_replacement = validate_numbers_replacement_lessons(numbers_replacement_lessons)

                    if cells[5].text.strip() != "":
                        row_data = f"{cells[4].text.strip()} {cells[5].text.strip()} (❗ замена)"
                    else:
                        row_data = f"{cells[4].text.strip()} (❗ замена)"

                    for number in valid_replacement:
                        group_data[number] = [number, row_data]

            print(group_data)
        else:
            raise Exception(f"Ошибка {response.status_code}")

    except Exception as e:
        print(e)
        return


def validate_numbers_replacement_lessons(numbers_replacement_lessons: str):
    list_result = []

    if numbers_replacement_lessons.find(",") != -1:
        number_list = numbers_replacement_lessons.split(",")
        for number in number_list:
            list_result.append(int(number.strip()))

    elif len(numbers_replacement_lessons) == 1:
        list_result.append(int(numbers_replacement_lessons))

    return list_result
