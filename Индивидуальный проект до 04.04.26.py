#Задание 1

products = {}

with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        name, count = line.strip().split()
        count = int(count)

        if name in products:
            products[name] += count
        else:
            products[name] = count

with open("corrected_data.txt", "w", encoding="utf-8") as file:
    for product, total in products.items():
        file.write(f"{product}: {total}\n")

total_items = sum(products.values())
most_popular = max(products, key=products.get)

print(total_items)
print(most_popular, products[most_popular])

#Задание 2

with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0
longest_line = ""

for line in lines:
    words = line.split()
    word_count += len(words)

    if len(line) > len(longest_line):
        longest_line = line

print(line_count)
print(word_count)
print(longest_line.strip())
