
#APITOKEN = '<616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ>'
#https://api.telegram.org/bot616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ/getUpdates
#https://api.telegram.org/bot616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ/sendMessage?chat_id=236704084&text=TestReply

#{"ok":true,"result":[{"update_id":959942309,
#"message":{"message_id":15,"from":{"id":236704084,"is_bot":false,"first_name":"Su-ann","username":"suanntaclaus","language_code":"en-GB"},"chat":{"id":236704084,"first_name":"Su-ann","username":"suanntaclaus","type":"private"},"date":1527910904,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}},{"update_id":959942310,
#"message":{"message_id":16,"from":{"id":236704084,"is_bot":false,"first_name":"Su-ann","username":"suanntaclaus","language_code":"en-GB"},"chat":{"id":236704084,"first_name":"Su-ann","username":"suanntaclaus","type":"private"},"date":1527910905,"text":"hello"}}]}
# - *- coding: utf- 8 - *-
# - *- coding: utf- 8 - *-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
  update.message.reply_text("I'm a bot, Nice to meet you!")
  
def convert_uppercase(bot, update):
  update.message.reply_text(update.message.text.upper())

def start_callback(bot, update, args):
    user_says = "hello".join(args)
    update.message.reply_text("You said: " + user_says)

def main():
  # Create Updater object and attach dispatcher to it
  updater = Updater("616484809:AAFyFLE0JHrxHOEsHXaa-gvGXYk7Tg19HxQ")
  dispatcher = updater.dispatcher
  print("Bot started")

  # Add command handler to dispatcher
  start_handler = CommandHandler('start',start)
  upper_case = MessageHandler(Filters.text, convert_uppercase)
  dispatcher.add_handler(start_handler)
  dispatcher.add_handler(upper_case)
  dispatcher.add_handler(CommandHandler(start_callback, pass_args=True))

  # Start the bot
  updater.start_polling()

  # Run the bot until you press Ctrl-C
  updater.idle()

if __name__ == '__main__':
  main()