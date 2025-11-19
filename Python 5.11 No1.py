def sort_numbers(text):
    numbers = text.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    numbers.sort()
    result = ""
    for n in numbers:
        result += str(n) + " "
    return result.strip()
s = "1 5 7 5 9 -5"
print(sort_numbers(s))
