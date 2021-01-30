import logging

from telegram.ext import Updater
from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters

import handlers
import config
from db import init_database

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger()
logger.setLevel(config.LOG_LEVEL or logging.DEBUG)


updater = Updater(token=config.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", handlers.start_handler))
dispatcher.add_handler(CommandHandler("total", handlers.total_handler))
dispatcher.add_handler(MessageHandler(Filters.photo, handlers.image_handler))
dispatcher.add_handler(MessageHandler(Filters.command, handlers.unknown_handler))

if __name__ == "__main__":
    logger.info("Starting up...")
    # init_database will not create new database/tables if they already exist
    init_database()
    updater.start_polling()
