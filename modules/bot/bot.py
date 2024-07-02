import asyncio
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from .keyboards import main_kb
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


# Объект бота
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


def start_bot():
    asyncio.run(main())


# Запуск процесса поллинга новых апдейтов
async def main():
    # await bot.delete_webhook(True)  Это позволяет пропускать сообщения, которые приходили в офлайн бота
    await dp.start_polling(bot)


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Стартует бот"""
    await message.answer(f"Здравствуйте {message.from_user.id}, вас приветствует элитный бот расписания",
                         reply_markup=main_kb(message.from_user.id))


@dp.message(F.text.lower() == "расписание")
@dp.message(Command("shedule"))
async def shedule(message: types.Message):
    """расписание"""
    await message.answer("Расписание на сегодня\n"
                         "1:""ноу")
