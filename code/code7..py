from time import sleep

class Hero():
    #конструктор класса
    def __init__(self, name, health, armor, damage):
        self.name = name
        self.health = health #число
        self.armor = armor #строка
        self.damage = damage
    #печать параметров персонажа
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor, '\n')



class Warrior(Hero):
    def hello(self):
        print(f"Верхом на коне появился воин {self.name}")
        print_info()
    def attack(self, enemy):
        print(f"Храбрый воин атакует мечом {Warrior}")
    

knight = Hero("Ричард", 50, 25, 10)
knight.print_info()
#далее запрограммируй классы-наследники суперкласса Hero