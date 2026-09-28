import time
# Задание 1

def hello(func):
    def wrapper():
        print("Начинаем...")
        func()
        print("Готово!")

    return wrapper
@hello
def first_test():
    print("Функция hello работает")
  
first_test()

# Задание 2
def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Время выполнения: {end - start:.4f} секунд")
    return wrapper

@timer
def second_test():
    time.sleep(1)
  
second_test()


# Задание 3
def retry(func):
    def wrapper():
        attempts = 3
        for i in range(attempts):
            try:
                return func()
            except Exception:
                print("Произошла ошибка. Повторяем...")
        raise RuntimeError("Действие не выполнилось после 3 попыток")
    return wrapper

number = 0

@retry
def third_test():
    global number

    number += 1
    print(f"Попытка {number}")

    if number < 3:
        raise ValueError("Ошибка")

    print("Действие успешно выполнено")

third_test()


# Задание 4
