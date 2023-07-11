import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from commands.echo import echo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    application = ApplicationBuilder().token('141879324:AAHselLyfdb8h1bjUSM9z7c_vI2vpSNvOyg').build()
    
    start_handler = CommandHandler('echo', echo)
    application.add_handler(start_handler)
    
    application.run_polling()