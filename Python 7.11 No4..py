def max_of_four(a, b, c, d):
    numbers = [a, b, c, d]
    if not all(isinstance(x, (int, float)) for x in numbers):
        return "Ошибка: все параметры должны быть числами."
    max = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
    return max
print(max_of_four(4, 11, 4, 7))
