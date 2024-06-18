import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Объект бота
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


def start_bot():
    asyncio.run(main())


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Стартует бот"""
    await message.answer("Здравствуйте, вас приветствует элитный бот расписания")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """расписание"""
    await message.answer("")
