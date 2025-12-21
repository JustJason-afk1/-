#Задача 1 math_utils.py

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n):   
        result *= i
    return result


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[:n]


def sum_of_digits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total


#Задача 2 string_utils.py

def is_palindrome(text):
    
    text = text.lower()
    return text == text[::-1]  


def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)

def reverse_string(text):
    return text[::-1]

