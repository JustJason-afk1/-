class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.hunger = 50

    def feed(self):
        self.hunger -= 10
        print(f"{self.name} покормили")

    def make_sound(self):
        print("Животное издает звук")

class Lion(Animal):
    def make_sound(self):
        print(f"{self.name} рычит")

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.name} кричит У-У-А-А-КК-ИИ-ББ-МЕМЕ")

lion = Lion("Помокнат", 5)
monkey = Monkey("Чершуша", 3)

lion.make_sound()
monkey.make_sound()

lion.feed()
print("Голод льва:", lion.hunger)
