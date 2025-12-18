inventory = []

print("Вы в лесу. Перед вами дом.")
choice = input("Зайти в дом? (да/нет): ").lower()

if choice == "да":
    print("В доме лежит ключ.")
    take = input("Взять ключ? (да/нет): ").lower()
    if take == "да":
        inventory.append("ключ")

    print("Вы видите запертую дверь.")
    open_door = input("Открыть дверь? (да/нет): ").lower()

    if open_door == "да" and "ключ" in inventory:
        print("\n ХОРОШАЯ КОНЦОВКА ")
        print("Вы нашли сокровище!")
    else:
        print("\n ПЛОХАЯ КОНЦОВКА ")
        print("Дверь не открылась.")
else:
    print("\n НЕЙТРАЛЬНАЯ КОНЦОВКА ")
    print("Вы ушли обратно в лес.")
