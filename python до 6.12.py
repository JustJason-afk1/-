# Программа учета времени учебы за неделю

total_hours = 0

while True:
    try:
        days = int(input("Введите количество учебных дней (1–7): "))
        if days <= 0:
            print("Количество дней должно быть положительным")
        elif days > 7:
            print("Количество дней не может превышать 7")
        else:
            break
    except ValueError:
        print("Ошибка ввода")

# Ввод часов учебы по дням
for i in range(1, days + 1):
    try:
        hours = int(input(f"Введите часы учебы за день {i}: "))
        if hours < 0:
            print("Отрицательное число, день засчитан как 0")  
        else:
            total_hours += hours
    except ValueError:
        print("Введено не число") 
# Вывод результата
print("Общее количество часов за неделю:", total_hours)
