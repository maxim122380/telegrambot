import telebot
import requests
token = "6695349813:AAEFSS0ZKKffmyumW0jQzGyTEcvd97OseNE"

bot = telebot.TeleBot(token)

def reqapi(ip):
    url = f"https://ipinfo.io{ip}/geo"
    r = requests.get(url).json()
    return r

def genetator_keybords(ListNameBTN, NumberColumns = 2):
    keyboards = telebot.types.ReplyKeyboardMarkup(row_width=NumberColumns, resize_keyboard=True)
    btn_names = [telebot.types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards


@bot.message_handler(commands=["start"])
def start(message):
    msg = bot.send_message(message.chat.id, "Hello", reply_markup=genetator_keybords(["Support", "Stop"]))
    bot.register_next_step_handler(msg, getip)

def getip(message):
    ip = message.text
    res = str(reqapi(ip))
    bot.send_message(message.chat.id, res)



if __name__ == '__main__':
    bot.infinity_polling()


