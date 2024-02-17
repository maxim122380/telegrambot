from random import *
def generate_password(lenght, chars):
    password = ""
    for i in range(lenght):
        password += choice(chars)
    return password

request = input("Хотите сгенерировать пароль?\n1-Да\n2-Нет\n--> ")
if request == "1":
    while request != "2":
        digits = "0123456789"
        lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
        uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        punctuation = "!@#$%^:&?*/.,"

        chars = ""
        lenght = int(input("Введите длину пароля: "))
        di = input("Добавить цифры?\n1-Да\n2-Нет\n--> ")
        if di == "1":
            chars += digits
        lowercase = input("Добавить буквы нижнего регистра?\n1-Да\n2-Нет\n--> ")
        if lowercase == "1":
            chars += lowercase_letters
        uppercase = input("Добавить буквы верхнего регистра?\n1-Да\n2-Нет\n--> ")
        if uppercase == "1":
            chars += uppercase_letters
        punct = input("Добавить спец. символы?\n1-Да\n2-Нет\n--> ")
        if punct == "1":
            chars += punctuation
        print(f"Ваш сгенерируемый пароль: {generate_password(lenght, chars)}")
        request = input("Хотите сгенерировать пароль?\n1-Да\n2-Нет\n--> ")

        
