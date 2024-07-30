from aiogram import types, F, Router
from aiogram.filters import CommandStart, Command

from .keyboards import main_kb, setting_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Здравствуйте {message.from_user.id}, вас приветствует элитный бот расписания",
                         reply_markup=main_kb(message.from_user.id))


@router.message(F.text.lower().contains("расписание"))
@router.message(Command("shedule"))
async def shedule(message: types.Message):
    await message.answer("Расписание на сегодня")
    
    
@router.message(F.text.lower().contains("настройки"))
@router.message(Command("settings"))
async def shedule(message: types.Message):
    await message.answer("Настройки бота... (пока что ничего нету)",
                         reply_markup=setting_kb(message.from_user.id))

@router.message(F.text.lower().contains("назад"))
async def shedule(message: types.Message):
    await message.answer("Возврат в главное меню...",
                         reply_markup=main_kb(message.from_user.id))

