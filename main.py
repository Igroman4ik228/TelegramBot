import json
import modules.bot.bot as bot
import modules.parser as parser
from threading import Thread
import logging.config
from logging import getLogger


with open("logging.conf.json") as file:
    config = json.load(file)

logging.config.dictConfig(config)
logger = getLogger()

if __name__ == "__main__":
    thParser = Thread(target=parser.main, args=())
    thParser.start()

    bot.start_bot()
