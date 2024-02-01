
import telebot

from telebot import types

bot = telebot.TeleBot('6762353695:AAFFXQQu4dsQFh1BA62fWIySTgpI5wt7-bE')


@bot.message_handler(commands=['start'])
def privet(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Приветствую, Дорогой друг !', reply_markup=markup)


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('Жми на кнопку, и я отправлю тебе название фрукта')

markup.add(item1)

fruit = ['яблоко', 'банан', 'груша', 'персик']




print('Work')
bot.infinity_polling()
