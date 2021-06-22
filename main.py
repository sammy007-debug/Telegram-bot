import constants as keys
from telegram.ext import *
import responses as r

print("I am ALIVE...")

def startCommand(update, context):
    update.message.reply_text('Type something random to get us started')

def helpCommand(update, context):
    update.message.reply_text('If you need some help ... just check the internet it is so easy these days')

def handleMessage(update, context):

    text = str(update.message.text).lower()



    # Bot response
    response = r.sampleResponse(text)

    update.message.reply_text(response)

def error(update, context):

    # print errors
    print(f"Update {update} cause error {context.error}")


# Run the programme
def main():
    updater = Updater(keys.API_Token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler("start", startCommand))
    dp.add_handler(CommandHandler("help", helpCommand))




    # Messages
    dp.add_handler(MessageHandler(Filters.text, handleMessage))

    dp.add_error_handler(error)


    # Run the bot
    updater.start_polling()
    updater.idle()


main()



