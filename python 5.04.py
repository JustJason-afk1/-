import json

with open("students.json", "r", encoding="utf-8") as f:
    students = json.load(f)

for student in students:
    print(student["name"], "-", student["avg_score"])

#json
[
    {"name": "Иван", "age": 19, "course": 1, "avg_score": 4.5},
    {"name": "Анна", "age": 20, "course": 2, "avg_score": 4.8},
    {"name": "Петр", "age": 18, "course": 1, "avg_score": 3.9}
]

#задание 2
import json

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

filtered = []

for product in products:
    if product["price"] > 1000 and product["in_stock"] == True:
        product["discount"] = product["price"] * 0.9  # минус 10%
        filtered.append(product)

for p in filtered:
    print(p["name"], "-", p["price"], "->", p["discount"])

#json
[
    {"name": "Ноутбук", "price": 1500, "category": "tech", "in_stock": true},
    {"name": "Мышка", "price": 500, "category": "tech", "in_stock": true},
    {"name": "Телефон", "price": 2000, "category": "tech", "in_stock": false},
    {"name": "Клавиатура", "price": 1200, "category": "tech", "in_stock": true}
]
