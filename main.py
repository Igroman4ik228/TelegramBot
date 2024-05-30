import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Объект бота
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("test1"))
async def cmd_test1(message: types.Message):
    await message.reply("Test 1")


# Хэндлер на команду /test2
async def cmd_test2(message: types.Message):
    await message.reply("Test 2")


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


# Запуск процесса поллинга новых апдейтов
async def main():
    print("Online")
    dp.message.register(cmd_test2, Command("test2"))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
