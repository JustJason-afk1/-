# МОДУЛЬ: string_utils

def UPPER(text):
    return text.upper()

def count_symbols(text):
    return len(text)

def is_palindrome(word):
    return word[::-1] == word

#string_utils

text = "Level"

print("Верхний регистр:", UPPER(text))
print("Количество символов:", count_symbols(text))
print("Палиндром:", is_palindrome(text))  


# МОДУЛЬ: random_utils

import random

def random_int(a, b):
    return random.randint(a, b)

def random_list(count):
    lst = []
    for i in range(count):
        lst.append(random.randint(1, 10))
    return lst

def shuffle_list(lst):
    random.shuffle(lst)
    return lst


 #random_utils

numbers = random_list(5)
print("Случайный список:", numbers)
print("Случайное число:", random_int(1, 10))
print("Перемешанный список:", shuffle_list(numbers))



# МОДУЛЬ: constants

PI = 3.14
G = 6.67 * 10 ** -11
C = 300000000


#constants

radius = 4
circle_length = PI * radius 
print("Длина окружности:", circle_length)

mass = 10
force = mass * G
print("Сила:", force)
