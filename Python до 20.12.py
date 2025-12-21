# Задача 1: Переводчик

def english(text):
    return text.replace("Привет", "Hello").replace("мир", "world")

def spanish(text):
    return text.replace("Привет", "Hola").replace("мир", "mundo")

def french(text):
    return text.replace("Привет", "Bonjour").replace("мир", "monde")

def translate(text, lang):
    langs = {
        "english": english,
        "spanish": spanish,
        "french": French 
        }
    func = langs.get(lang)
    if func:
        return func(text)
    else:
        return None  


# Задача 2: Генератор мира
def generate_world(size, seed):
    random.seed(seed)
    elements = ["~", "🌲", "⛰", "🏡"]
    world = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.choice(elements + [""]))
        world.append(row)
    return world



# Задача 3: Гибкий калькулятор
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return 0  
    return a / b

def calculate(a, b, operation):
    operations = {
        "addition": addition,
        "subtraction": subtraction,
        "multiplication": multiplication,
        "division": division
    }
    return operations[operation](a, b)
