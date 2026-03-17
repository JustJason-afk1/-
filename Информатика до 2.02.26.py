#Задание1 
class Weapon:
    def __init__(self, damage, modifier):
        self.damage = damage
        self._modifier = modifier

    def __apply_modifier(self):
        return self.damage * self._modifier

    def get_final_damage(self):
        print("Final damage:", self.damage * self._modifier) 
w = Weapon(10, 1.5)
w.get_final_damage()

#Задание2
class GameBank:
    def __init__(self, balance):
        self._balance = balance

    def __log_transaction(self, text):
        print("Log:", text)

    def deposit(self, amount):
        self._balance += amount
        self.__log_transaction("Deposit " + str(amount))

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.__log_transaction("Withdraw " + str(amount))
        else:
            print("Not enough money")
bank = GameBank(100)
bank.deposit(50)
bank.withdraw(200)
