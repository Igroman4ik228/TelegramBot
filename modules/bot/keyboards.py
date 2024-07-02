import os
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="Расписание")],
        [KeyboardButton(text="Предыдущее"), KeyboardButton(text="Следющее"),],
        [KeyboardButton(text="⚙️ Настройки")]
    ]

    admins = [int(x) for x in ''.join(os.getenv('ADMINS')).split(',')]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="Админ панель")])

    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   input_field_placeholder='Что вас интересует?')
    return keyboard
