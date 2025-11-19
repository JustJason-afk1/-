def print_odd_numbers(a, b):
    start = min(a, b) + 1
    end = max(a, b)
    odds = [num for num in range(start, end) if num % 2 != 0]
    if odds:
        print("Нечётные числа:", *odds)
    else:
        print("Нет нечётных чисел в этом диапазоне.")

print_odd_numbers(10, 3)
