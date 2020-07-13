import telebot
import subprocess
bot = telebot.TeleBot('токен')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Вкл_Скайп', 'ВЫКЛ')
keyboard1.row('Привет', 'Перезагрузка')






users_start = [40922918]  # последнее - id группы если бот что-то должен делать в группе
# Органичение выполнение команды start
@bot.message_handler(func=lambda message: message.chat.id not in users_start, commands=['start'])
def some(message):
    bot.send_message(message.chat.id, 'У Вас нет прав на выполнение данной команды')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'вкл_скайп':
        #subprocess.Popen(('start', 'C:/Users/User/PycharmProjects/bot/Skype_Ярлык'), shell = True)
        import os
        os.startfile('C:/Users/User/PycharmProjects/bot/Skype_Ярлык')
        bot.send_message(message.chat.id, 'Включил')
        

    elif message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель, Передай Дену БОЛЬШОЙ ПРИВЕТ!!!')
    elif message.text.lower() == 'перезагрузка':
        p = subprocess.Popen(shut, shell=True)
        bot.send_message(message.chat.id, 'Прощай, создатель')

shut = 'shutdown -r -t 0'

bot.polling()
