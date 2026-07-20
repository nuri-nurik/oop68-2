from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def get_health(self):
        return self.__health

    def set_health(self, amount):
        self.__health = amount

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        self.__health += 1
        print(f"{self.name} отдыхает. Здоровье увеличено до {self.__health}")

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию!")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")

warrior = Warrior(name="Артур", level=1, health=100, strength=20)
mage = Mage(name="Гэндальф", level=5, health=80, strength=50)
addassin = Assassin(name="Альтаир", level=3, health=90, strength=35)

warrior.greet()
warrior.attack()
warrior.rest()
print("-" * 30)

mage.greet()
mage.attack()
mage.rest()
print("-" * 30)

addassin.greet()
addassin.attack()
addassin.rest()
