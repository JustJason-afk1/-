# В списке целых, заполненном случайными числами,определить минимальный и максимальный элементы,посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать количество нулей.Результаты вывести на экран.
import random

numbers = []
for i in range(10):
    numbers.append(random.randint(-10, 10))

print("\nСписок чисел:", numbers)

min_num = numbers[0]
max_num = numbers[0]
count_pos = 0
count_neg = 0
count_zero = 0

for num in numbers:
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    if num > 0:
        count_pos += 1
    elif num < 0:
        count_neg += 1
    else:
        count_zero += 1

print("Минимальное число:", min_num)
print("Максимальное число:", max_num)
print("Положительные числа:", count_pos)
print("Отрицательные числа:", count_neg)
print("Нулей:", count_zero)