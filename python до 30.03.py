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
