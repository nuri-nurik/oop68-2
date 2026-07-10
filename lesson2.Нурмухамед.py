import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print("Привет!")

    def attack(self):
        print("Герой наносит удар")

    def rest(self):
        self.health = self.health + 10


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")


warrior_obj = Warrior("Конан", 5, 150, 18, 100)
mage_obj = Mage("Гэндальф", 7, 90, 6, 150)
assassin_obj = Assassin("Эцио", 6, 110, 14, 85)


user_choice = input("Выберите героя: Warrior / Mage / Assassin: ")

heroes_list = ["Warrior", "Mage", "Assassin"]
computer_choice = random.choice(heroes_list)

print("Вы выбрали:", user_choice)
if user_choice == "Warrior":
    warrior_obj.attack()
elif user_choice == "Mage":
    mage_obj.attack()
elif user_choice == "Assassin":
    assassin_obj.attack()

print("Противник:", computer_choice)
if computer_choice == "Warrior":
    warrior_obj.attack()
elif computer_choice == "Mage":
    mage_obj.attack()
elif computer_choice == "Assassin":
    assassin_obj.attack()


if user_choice == computer_choice:
    print("Ничья!")
elif user_choice == "Warrior" and computer_choice == "Assassin":
    print("Warrior победил!")
elif user_choice == "Assassin" and computer_choice == "Mage":
    print("Assassin победил!")
elif user_choice == "Mage" and computer_choice == "Warrior":
    print("Mage победил!")
else:
    print(computer_choice, "победил!")
































































