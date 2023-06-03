# Some library we need to use 
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import WeatherClass 


# Basic configs(don't change that)
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
    
# function for handler unknown command
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Wrong command")

# help function
async def help(update : Update, context : ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text= "/start : Starting bot\n/weather City : showing general and feelslike of today ")

# Show weather 
async def show_weather(update : Update, context : ContextTypes.DEFAULT_TYPE):
    try : 
        input_city = context.args[0]
        general_weather, feelslike = WeatherClass.Weather(input_city)
        await context.bot.send_message(chat_id=update.effective_chat.id, text= f" Today's general weather : {general_weather}\nToday's feelslike : {feelslike} °C" )
    except : 
        pass

# Appliction builder 
application = ApplicationBuilder().token('5514096270:AAFr30Wcg0MTYMeZ-FjKH4vTBZP0K-Y8Pb0').build()

""" We made some handler for doing simple works 
start and help handler is simple to know 
echo handler works on client messages without command, it run help command to the client and after that client know the right commands """  

start_handler = CommandHandler('start', start)

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), help)
   
help_handler = CommandHandler('help',help)

weather_handler = CommandHandler('weather',show_weather)

application.add_handler(start_handler)

application.add_handler(echo_handler)

application.add_handler(help_handler)

application.add_handler(weather_handler)
 
        
application.run_polling()