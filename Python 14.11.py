import random

#Создание функции генерации одного пароля
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    symbols = ""

    if use_upper:
        symbols += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_lower:
        symbols += "abcdefghijklmnopqrstuvwxyz"
    if use_digits:
        symbols += "0123456789"
    if use_special:
        symbols += "!@#$%^&*()"

    if symbols == "":
        return "Ошибка: не выбраны символы!"

    password = ""
    for i in range(length):
        password += random.choice(symbols)

    return password


# Проверка на надёжность пароля
def check_strength(password):
    score = 0

    if len(password) >= 12:
        score += 1

    # Проверка на наличие разных типов символов
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for c in password:
        if c.isupper():
            has_upper = True
        if c.islower():
            has_lower = True
        if c.isdigit():
            has_digit = True
        if c in "!@#$%^&*()":
            has_special = True

    types = has_upper + has_lower + has_digit + has_special

    # Надёжность пароля
    if score == 1 and types == 4:
        return "Сильный"
    elif types >= 2 and len(password) >= 8:
        return "Средний"
    else:
        return "Слабый"


# Генерация нескольких уникальных паролей
def generate_unique_passwords(count, length, use_upper, use_lower, use_digits, use_special):
    passwords = []

    while len(passwords) < count:
        pwd = generate_password(length, use_upper, use_lower, use_digits, use_special)

        if pwd not in passwords:
            passwords.append(pwd)

    return passwords


# Пример работы
p = generate_password(12, True, True, True, True)
print("Пароль:", p)
print("Надёжность:", check_strength(p))

print("\nУникальные пароли:")
lst = generate_unique_passwords(5, 10, True, True, True, True)
for x in lst:
    print(x)