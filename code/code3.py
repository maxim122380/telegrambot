from random import *
words = ["москва","ковров","казань","тула"]

def get_ask():
    return choice(words)

def play(word):
    print("Я загадал слово, попробуй угадать его!")
    word_ask = "_" * len(word)
    hp = 6
    win = False
    print("Загаданное слово", word_ask)
    while not win and hp > 0:
        ask = input("Введите букву: ").lower()
        
        if ask in word:
            print("Отлично! Ты угадал букву!")
            word_as_list = list(word_ask)
            indices = [i for i in range(len(word)) if word[i] == ask]
            for index in indices:
                word_as_list[index] = ask
                word_ask = "".join(word_as_list)
                if "_" not in word_ask:
                    win = True
          
        else:
            hp -= 1
            print(f"Тебе не удалось угадать букву, осталось попыток {hp}")
        print(word_ask)



answer = input("Сыграем в игру?\n1-Да\n2-Нет\n-> ")
while answer != "2":
    if answer == "1":
        play(get_ask())
    else:
        break 
    answer = input("Сыграем ещё раз?\n1-Да\n2-Нет\n-> ")

