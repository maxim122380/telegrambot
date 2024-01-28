import telebot
import requests
token = "6695349813:AAEFSS0ZKKffmyumW0jQzGyTEcvd97OseNE"

bot = telebot.TeleBot(token)

def reqapi(ip):
    url = f"https://ipinfo.io{ip}/geo"
    r = requests.get(url).json()
    return r


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_support = telebot.types.KeyboardButton(text="Написать в поддержку") 
    button1 = telebot.types.KeyboardButton(text="Кнопка 1")
    button2 = telebot.types.KeyboardButton(text="Кнопка 2")
    button3 = telebot.types.KeyboardButton(text="Кнопка 3")
    keyboard.add(button_support, button1, button2, button3)
    msg = bot.send_message(message.chat.id, "hello", reply_markup=keyboard)
    bot.register_next_step_handler(msg, getip)

def getip(message):
    ip = message.text
    res = str(reqapi(ip))
    bot.send_message(message.chat.id, res)



if __name__ == '__main__':
    bot.infinity_polling()


