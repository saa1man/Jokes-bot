import logging
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler
import requests
import json

BOT_TOKEN = "PUT YOUR BOT TOKEN HERE"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Commands Functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to Jokes bot by @Essuuii.\nType /help for a list of available commands.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply = f"Your message '{update.message.text}' is not a command. Please type /help for a list of available commands."
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=reply)

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    command_list = [
        "/start - Start the bot",
        "/help - Get a list of available commands",
        "/any - Tell a random joke of any type",
        "/programming - Tell a random programming joke",
        "/misc - Tell a random miscellaneous joke",
        "/dark - Tell a random dark joke",
        "/pun - Tell a random pun joke",
        "/spooky - Tell a random spooky joke",
        "/christmas - Tell a random Christmas joke"
    ]
    help_text = "Here are the available commands:\n\n" + "\n".join(command_list)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=help_text)

async def any(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Any")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def programming(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Programming")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def misc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Misc")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def dark(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Dark")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def pun(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Pun")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def spooky(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Spooky")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def christmas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    joke = get_random_joke(joke_type="Christmas")
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=joke)

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Sorry, I didn't understand that command.\nPlease type /help for a list of available commands.")

# Main Function
def get_random_joke(joke_type):
    url = f"https://v2.jokeapi.dev/joke/{joke_type}"
    response = requests.get(url)
    joke_data = json.loads(response.text)

    if joke_data["type"] == "single":
        joke = joke_data["joke"]
    elif joke_data["type"] == "twopart":
        setup = joke_data["setup"]
        delivery = joke_data["delivery"]
        joke = f"{setup} {delivery}"
    else:
        joke = "Sorry, I couldn't find a joke for you."

    return joke


if __name__ == '__main__':
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Commands Handlers
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)
    
    any_handler = CommandHandler('any', any)
    application.add_handler(any_handler)
    
    programming_handler = CommandHandler('programming', programming)
    application.add_handler(programming_handler)
    
    misc_handler = CommandHandler('misc', misc)
    application.add_handler(misc_handler)
    
    dark_handler = CommandHandler('dark', dark)
    application.add_handler(dark_handler)
    
    pun_handler = CommandHandler('pun', pun)
    application.add_handler(pun_handler)
    
    spooky_handler = CommandHandler('spooky', spooky)
    application.add_handler(spooky_handler)

    christmas_handler = CommandHandler('christmas', christmas)
    application.add_handler(christmas_handler)
    
    # Other Handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)
    
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(echo_handler)

    # Run App
    application.run_polling()