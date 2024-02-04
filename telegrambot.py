import requests
import telebot
from telebot import types
from environs import Env

env = Env()
env.read_env()
token = env("TOKEN")

bot = telebot.TeleBot(token)

bot.message_handler(commands=["hello"])
def start(message):
    keyboard = types.InlineKeybordMarkup()
    keyboard.add(types.InlineKeybordButton("Play", callback_data="play"))
    bot.send_message(message.chat.id, "Меню программы:", reply_markup=keyboard)

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
        bot.edit_message_reply_markup(chat_id=call.message.id, message_id=call.message.message_id, reply_markup=markup)


def getinfo(ip: str) -> dict:
    url = f'https://ipinfo.io/{ip}/geo'
    r = requests.get(url).json()
    return r

def getip(message):
    ip = message.text
    res = str(getinfo(ip))
    bot.send_message(message.chat.id, res)


def genetator_keybords(ListNameBTN, NumberColumns = 2):
    keyboards = telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns, resize_keyboard=True)
    btn_names = [telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello", reply_markup=genetator_keybords(["Support(поддержка)", "Stop(стоп)", "IP"]))

@bot.message_handler(func = lambda x : x.text)
def text(message):
    text = message.text
    if text == "Support(поддержка)":
        bot.send_message(message.chat.id, "Я вас слушаю")
    elif text == "Stop(стоп)":
        bot.send_message(message.chat.id, "До свидания")
    elif text == "IP":
        msg = bot.send_message(message.chat.id, "Напишите свой ip")
        bot.register_next_step_handler(msg, message_ip)

def message_ip(message):
    ip = message.text
    res = str(getinfo(ip))
    bot.send_message(message.chat.id, res)


if __name__ == '__main__':
    bot.infinity_polling()