import telebot
from telebot import types


token = ""

bot = telebot.TeleBot(token)

bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.InlineKeybordMarkup()
    keyboard.add(types.InlineKeybordButton(text="Play", callback_data="play"))
    bot.send_message(message.chat.id, text="Меню программы:", reply_markup=keyboard)

bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "play":
        markup = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Stop", callback_data="stop")
        btn2 = types.InlineKeyboardButton("Cool", callback_data="cool")
        btn3 = types.InlineKeyboardButton("-_-", callback_data="add")
        markup.add(btn1, btn2, btn3)
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
    elif call.data == "stop":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Play", callback_data="play"))
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)

if __name__ == '__main__':
    bot.infinity_polling()