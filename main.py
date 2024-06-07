import modules.Bot as Bot
import modules.Parser as Parser
from threading import Thread

if __name__ == "__main__":
    thParser = Thread(target=Parser.main, args=())
    thParser.start()

    Bot.start_bot()

