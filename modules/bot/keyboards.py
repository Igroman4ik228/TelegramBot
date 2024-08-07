from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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


def admin_kb():
    kb_list = [
        [KeyboardButton(text="Глобальное сообщение"), KeyboardButton(text="Принудительный парсинг"),],
        [KeyboardButton(text="Вывод лог ошибок")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb_list,
                                   resize_keyboard=True,
                                   input_field_placeholder="Выберите пункт меню")
    return keyboard


# todo: callback ToggleNotification, callback WriteDefaultSchedule
def setting_kb(user_telegram_id: int):
    
    notification_text = "🔔 Уведомление включены"
    kb_list = [
        [InlineKeyboardButton(text=notification_text, callback_data="ToggleNotification"), InlineKeyboardButton(text="Вывести обычное расписание", callback_data="WriteDefaultSchedule")],
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=kb_list, 
                                    text="Настройки")
    return keyboard
