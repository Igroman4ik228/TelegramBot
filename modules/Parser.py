import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://menu.sttec.yar.ru/timetable/rasp_first.html'
    response = requests.get(url)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('table')

            if data is None:
                raise Exception("Не найдена таблица с расписанием")

        except Exception as e:
            print(e)
            return

        rows = data.find_all('tr')
        if rows:
            rows = rows[1:]  # Skip the first row if it's a header
        else:
            raise Exception("Не найдены строки в таблице")
        for row in rows:
            cells = row.find_all('td')
            for cell in cells:
                print(cell.text)

    else:
        raise Exception(f"Ошибка {response.status_code}")
