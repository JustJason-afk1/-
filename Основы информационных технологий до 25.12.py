# Даны группы студентов
math_students = {"Анна", "Борис", "Виктор", "Дарья", "Елена"}
physics_students = {"Виктор", "Георгий", "Дарья", "Иван", "Ксения"}
cs_students = {"Анна", "Виктор", "Елена", "Иван", "Мария"}

# 1. Студенты, посещающие все три курса
all_three = math_students & physics_students & cs_students

# 2. Студенты, посещающие только математику
only_math = math_students - physics_students - cs_students

# 3. Все уникальные студенты
all_students = math_students | physics_students | cs_students

# 4. Студенты, посещающие ровно два курса
two_courses = (
    (math_students & physics_students) |
    (math_students & cs_students) |
    (physics_students & cs_students)
) - all_three

# Вывод результатов
print("1. Посещают все три курса:", all_three)
print("2. Посещают только математику:", only_math)
print("3. Все уникальные студенты:", all_students)
print("4. Посещают ровно два курса:", two_courses)
