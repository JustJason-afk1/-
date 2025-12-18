#Задача 1. Сумма элементов списка

numbers = [1, 2, 3, "4", 5]

try:
    total = 0
    for n in numbers:
        total += n 
    print("Сумма:", total)
except TypeError:
    print("Ошибка: в списке есть нечисловой элемент")


#Задача 3. Поиск максимального элемента

numbers = [3, 7, 2, 9, 1, 5, 4, 8, 6, 0]

try:
    max_num = numbers[0]
    for i in numbers:
        if i > max_num:
            max_num = i
    print("Максимальный элемент:", numbers) 
except IndexError:
    print("Ошибка: список пуст")
`

#Задача 4. Проверка наличия элемента

numbers = [10, 20, 30, 40, 50]

try:
    x = int(input("Введите число: "))
    if x in numbers:
        print("Число есть в списке")
    else:
        print("Числа нет в списке")
except ValueError:
    print("Ошибка ввода")
