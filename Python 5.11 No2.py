def find_min_index(list_of_numbers):
    minimum_value = list_of_numbers[0]
    minimum_index = 0
    current_index = 0

    while current_index < len(list_of_numbers):
        if list_of_numbers[current_index] < minimum_value:
            minimum_value = list_of_numbers[current_index]
            minimum_index = current_index
        current_index += 1

    return minimum_index
numbers = [12, -3, 7, 0, 25, -10]
print(find_min_index(numbers))