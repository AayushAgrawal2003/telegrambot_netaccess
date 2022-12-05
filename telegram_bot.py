import os
import telebot
# from dotenv import load_dotenv
# load_dotenv()

import dotenv
import time
import schedule
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

from test import check_ip,netaccess


API_KEY = os.getenv('API_KEY')


#print(API_KEY)
bot = telebot.TeleBot(API_KEY)

if __name__ == '__main__':

    @bot.message_handler(commands = ['start'])
    def welcome(message):
        bot.send_message(message.chat.id,'Welocome! Use /ip for current ip adress and /netacess to perform netaccess')


    @bot.message_handler(commands = ['ip'])

    def ip(message):
        old_ip = os.getenv("IP")
        bot.reply_to(message,'Loading...')

        new_ip = check_ip()
        if old_ip != new_ip:
            bot.send_message(message.chat.id,'ip changed, new ip = ' + new_ip)
            os.environ["IP"] = new_ip
            dotenv.set_key(dotenv_file, "IP", os.environ["IP"])

            #old_ip = new_ip
        else:
            bot.send_message(message.chat.id,'ip not changed, current ip = ' + new_ip)

    @bot.message_handler(commands = ['alive'])

    def alive(message):
        bot.send_message(message.chat.id,'Use /ip to get current ip')


    @bot.message_handler(commands = ['netaccess'])

    def Netaccess(message):
        new_ip = netaccess()
        bot.send_message(message.chat.id,'netaccess done, new ip = ' + new_ip)


    bot.polling()
