import json
import modules.bot.bot as bot
import modules.parser as parser
from threading import Thread
import logging.config
from logging import getLogger


with open("logger.conf.json") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()

if __name__ == "__main__":
    thParser = Thread(target=parser.main_parse, args=())
    thParser.start()

    bot.start_bot()
    