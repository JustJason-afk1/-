def sort_numbers(s):
    numbers = [int(x) for x in s.split()]
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return " ".join(str(x) for x in numbers)

text = "5 2 9 1 7"
print(sort_numbers(text))
