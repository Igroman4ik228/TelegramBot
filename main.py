import json
import modules.bot.bot as bot
import modules.parser as parser
from threading import Thread
import logging.config
from logging import getLogger

# from modules.dbcontext import session
# from modules.repositories.result_repository import ResultRepository
# from modules.repositories.schedule_repository import ScheduleRepository
# from modules.repositories.users_repository import UserRepository

with open("logger.conf.json") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()

if __name__ == "__main__":
    thParser = Thread(target=parser.main, args=())
    thParser.start()

    bot.start_bot()
