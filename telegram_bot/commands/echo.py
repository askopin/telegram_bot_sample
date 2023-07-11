from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import MessageEntityType
from ..helpers.string_helpers import StringRange, clear_ranges

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_ranges = [StringRange(e.offset, e.length) for e 
                        in update.message.entities
                        if e.type == MessageEntityType.BOT_COMMAND]
    reply_text = clear_ranges(update.message.text, command_ranges)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=reply_text
    )