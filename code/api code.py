import random
import time
player = {
    "name" : "player",
    "hp" : 5,
    "dmg" : 1,
}

boss = {
    "name" : "Ворон",
    "hp" : 10,
    "dmg" : 2,
}



locate = ["мрачном", "светлом", "старом"]
loc = ['доме', 'лесу', 'особняке']

player["name"] = input("Введите имя вашего игрока:")

def fight():
    while player["hp"] > 0 and boss["hp"] > 0:
        time.sleep(2)
        dam = random.randint(1, 3) * player["dmg"]
        boss["hp"] -= dam
        print(f"Вы нанесли {dam} урона!")


while True:
    print(f"Добро пожаловать в игру, {player['name']}!")
    time.sleep(2)
    print(f"Вы появились в {random.choice(locate)} {random.choice(loc)}...")
    print(f"Перед вами появился босс {boss['name']}")
    fight()



    break