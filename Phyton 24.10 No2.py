#Сделать Список
a = []
for i in range(10):
    a.append(random.randint(-10, 10))

print("Список:", a)

even = []
odd = []
neg = []
pos = []

for x in a:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

    if x < 0:
        neg.append(x)
    if x > 0:
        pos.append(x)

print("Четные:", even)
print("Нечетные:", odd)
print("Отрицательные:", neg)
print("Положительные:", pos)