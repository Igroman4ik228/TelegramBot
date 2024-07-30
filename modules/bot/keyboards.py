from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


def main_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="🗓 Расписание")],
        [KeyboardButton(text="⬅️ Предыдущее"), KeyboardButton(text="Следующее ➡️"),],
        [KeyboardButton(text="⚙️ Настройки")]
    ]

    admins = [int(x) for x in ''.join(os.getenv('ADMINS')).split(',')]
    if user_telegram_id in admins:
        kb_list.append([KeyboardButton(text="🔐 Админ панель")])

    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")
    return keyboard

def setting_kb(user_telegram_id: int):
    kb_list = [
        [KeyboardButton(text="🔔🔕 Уведомление"), KeyboardButton(text="Смена роли"),],
        [KeyboardButton(text="🔙 Назад")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")
    return keyboard