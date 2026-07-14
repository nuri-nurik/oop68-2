import random

class Hero:
    def __init__(self, name: str, lvl: int, hp: float):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        return f"{self.name} готов к бою!"


class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: float, mp: float):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        return f"Маг {self.name} кастует заклинание! MP: {self.mp}"


class WarriorHero(MageHero):
    def action(self):
        return f"Воин {self.name} рубит мечом! Уровень: {self.lvl}"


class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance: float, password: str):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password: str) -> bool:
        return password == self.__password

    @property
    def full_info(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def get_bank_name(self) -> str:
        return self.bank_name

    def bonus_for_level(self) -> int:
        return self.hero.lvl * 12

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) is not type(other.hero):
            return "Ошибка: Нельзя сложить счета героев разных классов!"
        return self._balance + other._balance

    def __eq__(self, other):
        return (type(self.hero) is type(other.hero) and
                self.hero.lvl == other.hero.lvl)


class KGSms:
    def send_otp(self, phone: str):
        code = random.randint(1000, 9999)
        return f"Код {code} отправлен на номер {phone}"


mage1 = MageHero("Merlin", lvl=40, hp=100, mp=200)
mage2 = MageHero("Merlin", lvl=50, hp=100, mp=150)
warrior1 = WarriorHero("Conan", lvl=48, hp=300, mp=0)

print(mage1.action())
print(warrior1.action())

acc1 = BankAccount(hero=mage1, balance=7000, password="password123")
acc2 = BankAccount(hero=mage2, balance=4500, password="password456")
acc3 = BankAccount(hero=warrior1, balance=2000, password="password789")

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)
print("Сумма мага и воина:", acc1 + acc3)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)

sms = KGSms()
print("\n", sms.send_otp("+996000000000"))
