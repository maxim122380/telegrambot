from random import *
def cube():
    return randint(1,6)                 
print("Добро пожаловать в игру кости💰!")
start_money = 1000
print(f"Ваш начальный баланс: {start_money}💲")
x = 0
while True:
    gamer = input("Бросить кубики🎲?\n1-Да\n2-Нет\n🢫 ")
    bid = int(input("Введите вашу ставку в 💲: "))
    if bid <= start_money:
        if gamer == "1":
            gamer_cube = cube()
            computer_cube = cube()
            if gamer_cube > computer_cube:
                x += 1    #подсчёт выигреший
                money = bid * 2
                print(f"Поздравляю, вы выиграли {money}💲! Ваше число было: {gamer_cube}. Число компьютера было: {computer_cube}.")
            elif gamer_cube < computer_cube:
                money1 = bid // 2
                print(f"Вы проиграли {money1}💲. Ваше число было: {gamer_cube}. Число компьютера было: {computer_cube}.")
            else:
                print(f"Ничья🤝! Ваш баланс: {start_money}💲. Ваше число было: {gamer_cube}. Число компьютера было: {computer_cube}.")
        elif gamer == "2":
            break
    
        if x == 5:
            print(f"Ваш суточный лимит достигнут. Вы выграли 5 раз и больше не можете играть! До свидания.")
            break

