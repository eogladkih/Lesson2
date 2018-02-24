from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, ephem, datetime 

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
  #  print('Вызван /start')
    text = 'Ку-ку'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

#определяем созвездие в котором находится планета
def define_constellation(bot, update, args):
    
    planet_name = ''.join(args)
  
    planet_object = getattr(ephem, planet_name)
    cons=ephem.constellation(planet_object(datetime.datetime.now()))
    update.message.reply_text(cons)

#не понятно кчто делать с if ((((    




def main():
    updater = Updater("INSERT_ID")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
#handler для обработки команд /Planet
    dp.add_handler(CommandHandler("planet", define_constellation, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    updater.start_polling()
    updater.idle()

main()
