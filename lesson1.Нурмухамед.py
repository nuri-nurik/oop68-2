class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1

hero1 = Hero(name="Артас", level=10, health=100, strength=20)
hero2 = Hero(name="Тралл", level=8, health=85, strength=15)

print("--- Первый герой ---")
hero1.greet()
hero1.attack()
hero1.rest()
print(f"Новые характеристики {hero1.name}: Сила = {hero1.strength}, Здоровье = {hero1.health}")

print("\n--- Второй герой ---")
hero2.greet()
hero2.attack()
hero2.rest()
print(f"Новые характеристики {hero2.name}: Сила = {hero2.strength}, Здоровье = {hero2.health}")