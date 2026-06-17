with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

data = {}

for line in lines:
    line = line.strip()
    if not line:
        continue

    name, count = line.split(":")
    name = name.strip()
    count = int(count.strip())

    if name in data:
        data[name] += count
    else:
        data[name] = count

with open("corrected_data.txt", "w", encoding="utf-8") as f:
    for name, count in data.items():
        f.write(f"{name}: {count}\n")

total = sum(data.values())
most_popular = max(data, key=data.get)

print("Общее кол-во товаров:", total)
print("Самый популярный товар:", most_popular)

#задние 2
with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

word_count = 0
longest_line = ""

for line in lines:
    words = line.split()
    word_count += len(words)

    if len(line) > len(longest_line):
        longest_line = line

print("Общее кол-во слов:", word_count)
print("Общее кол-во строк:", len(lines))
print("Самая длинная строка:", longest_line.strip())
