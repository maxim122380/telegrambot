water_counter = 2
meal_counter = 1
light_counter = 2

class Vegetable:
    def __init__(self, name_v, water, meal, light):
        self.name_v = name_v
        self.water = water
        self.meal = meal
        self.light = light
    def print_info(self):
        print(f"Вид образца: {self.name_v}")
        print(f"Обеспеченность водой: {self.water}")
        print(f"Обеспеченность питательными веществами: {self.meal}")
        print(f"Обеспеченность светом: {self.light}")

class Assistant:
    def __init__(self, name, post):
         self.name = name
         self.post = post

    def print_info(self):
        print(f"Имя:{self.name}, должность: {self.post}")

def watering():
    print("Полив!🚿")
    water_counter += 1
def no_watering():
    water_counter -= 1
    

def nutrient_availability():
    print("Внесение удобрения🌱!")
    meal_counter += 1
def no_nutrient_availability():
    meal_counter -= 1
    
def enabling_additional_lighting():
    print("Включено дополнительное освещение🌤!")
    light_counter += 1
def no_enabling_additional_lighting():
    light_counter -= 1
        

def work():
    x = input("Вы хотите полить опытный образец?\n").lower()
    if x == "да":
        watering()
    elif x == "нет":
        no_watering()
    y = input("Вы хотите внести удобрение для опытного образца?\n").lower()
    if y == "да":
        nutrient_availability()
    elif y == "нет":
        no_nutrient_availability()
    z = input("Вы хотите включить дополнительное освещение для опытного образца?\n").lower()
    if z == "да":
        enabling_additional_lighting()
    elif z == "нет":
        no_enabling_additional_lighting()

def final():
    print(f"Вид образца: Кукуруза")
    print(f"Обеспеченность водой: {water_counter}")
    print(f"Обеспеченность питательными веществами: {meal_counter}")
    print(f"Обеспеченность светом: {light_counter}")

vegetabl1 = Assistant(" Александр", "стажер.") 
vegetabl1.print_info()
vegetabl = Vegetable("Кукуруза", water_counter, meal_counter, light_counter)
vegetabl.print_info()
work()
final()







