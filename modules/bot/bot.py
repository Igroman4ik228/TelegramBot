from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv
import asyncio
import os

from .handlers import router

load_dotenv(find_dotenv())


def start_bot():
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот выключен")
        return


async def main():
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_routers(router)
    # await bot.delete_webhook(True)  Это позволяет пропускать сообщения, которые приходили в офлайн бота
    await dp.start_polling(bot)

