a = []
b = []

for i in range(10):
    a.append(random.randint(0, 20))

for i in range(10):
    b.append(random.randint(0, 20))

print("Список A:", a)
print("Список B:", b)

# 1) элементы обоих списков
third1 = a + b
print("\n1) Элементы обоих списков:")
print(third1)

# 2) элементы обоих списков без повторений
third2 = []
for x in a + b:
    if x not in third2:
        third2.append(x)

print("\n2) Без повторений:")
print(third2)

# 3) элементы общие для двух списков
third3 = []
for x in a:
    if x in b and x not in third3:
        third3.append(x)

print("\n3) Общие элементы:")
print(third3)

# 4) уникальные элементы каждого списка
third4 = []
for x in a:
    if x not in b and x not in third4:
        third4.append(x)

for x in b:
    if x not in a and x not in third4:
        third4.append(x)

print("\n4) Уникальные элементы каждого списка:")
print(third4)

# 5) минимальное и максимальное значение каждого списка
third5 = [min(a), max(a), min(b), max(b)]

print("\n5) Минимумы и максимумы:")
print(third5)
