import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from .commands.echo import echo
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_API_TOKEN = os.environ.get("BOT_API_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_API_TOKEN).build()
    
    start_handler = CommandHandler('echo', echo)
    application.add_handler(start_handler)
    
    application.run_polling()