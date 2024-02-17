mag = {
    "молоко" : 150,
    "хлеб" : 50,
    "лимонад" : 100,
    "шоколад" : 80
}
summa = 0
x = input("Что вы взяли (всё - закончить): ").lower()
while x != "всё":
    k = int(input("В каком количестве: "))
    if x == "молоко":
        summa += mag[x] * k
    elif x == "хлеб":
        summa += mag[x] * k
    elif x == "лимонад":
        summa += mag[x] * k
    elif x == "шоколад":
        summa += mag[x] * k
    x = input("Что вы взяли (всё - закончить): ").lower()

print(f"К оплате: {summa} рублей.")
































