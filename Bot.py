import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#starting bot function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot for showing current weather to you")

# function for non-command replay
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="please write a command to use")

# function for convert lower case sentences to upper case 
async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# function for handler unknown command
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Wrong command")

# help function
async def help(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= "/start : Starting bot\n/caps something : Convert sentence to upper case")


if __name__ == '__main__':
    application = ApplicationBuilder().token('5514096270:AAFr30Wcg0MTYMeZ-FjKH4vTBZP0K-Y8Pb0').build()
        
    start_handler = CommandHandler('start', start)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    caps_handler = CommandHandler('caps',caps)
   
    help_handler = CommandHandler('help',help)

    application.add_handler(start_handler)

    application.add_handler(echo_handler)

    application.add_handler(caps_handler)

    application.add_handler(help_handler)
 
        
    application.run_polling()