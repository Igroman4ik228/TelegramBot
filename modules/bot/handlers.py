from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

from .keyboards import main_kb, setting_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуйте {message.from_user.id}, вас приветствует элитный бот расписания",
                         reply_markup=main_kb(message.from_user.id))


@router.message(F.text.lower().contains("расписание"))
@router.message(Command("schedule"))
async def schedule(message: types.Message):
    await message.answer("Расписание на сегодня") # Из бд 
    
    
@router.message(F.text.lower().contains("настройки"))
@router.message(Command("settings"))
async def setting(message: types.Message):
    await message.reply("Настройки бота...",
                         reply_markup=setting_kb())

# todo
@router.callback_query(lambda c: c.data == 'Notification')
async def process_notification_callback(callback_query: types.CallbackQuery):
    await callback_query.answer()
    await callback_query.message.answer("Вы нажали кнопку уведомлений.")

