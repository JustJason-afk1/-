#Cделать список
import random

a = []
for i in range(10):
    a.append(random.randint(-10, 10))

print("Список:", a)

# 1. сумма отрицательных
sum_neg = 0
for x in a:
    if x < 0:
        sum_neg = sum_neg + x

# 2. сумма четных
sum_even = 0
for x in a:
    if x % 2 == 0:
        sum_even = sum_even + x

# 3. сумма нечетных
sum_odd = 0
for x in a:
    if x % 2 != 0:
        sum_odd = sum_odd + x

# 4. произведение элементов с индексами кратными 3
pr3 = 1
for i in range(len(a)):
    if i % 3 == 0:
        pr3 = pr3 * a[i]

# 5. ищу min и max САМ (как студент)
mn = a[0]
mx = a[0]
i_mn = 0
i_mx = 0

for i in range(len(a)):
    if a[i] < mn:
        mn = a[i]
        i_mn = i
    if a[i] > mx:
        mx = a[i]
        i_mx = i

# делаю произведение между ними
pr_between = 1
start = 0
end = 0

if i_mn < i_mx:
    start = i_mn
    end = i_mx
else:
    start = i_mx
    end = i_mn

for i in range(start + 1, end):
    pr_between = pr_between * a[i]

# 6. сумма между первым и последним положительными
first = -1
last = -1

for i in range(len(a)):
    if a[i] > 0:
        if first == -1:
            first = i
        last = i

sum_pos = 0
if first != -1 and last != -1 and first < last:
    for i in range(first + 1, last):
        sum_pos = sum_pos + a[i]

print("Сумма отрицательных:", sum_neg)
print("Сумма четных:", sum_even)
print("Сумма нечетных:", sum_odd)
print("Произведение индексов % 3:", pr3)
print("Мин =", mn, "Макс =", mx)
print("Произведение между ними:", pr_between)
print("Сумма между первым и последним положительными:", sum_pos)
