import requests
import json

book_name = input("Введите название книги: ")
 
query = book_name.replace(" ", "+")

url = f"https://www.googleapis.com/books/v1/volumes?q={query}"

response = requests.get(url)
data = response.json()

print("\n=== РЕЗУЛЬТАТ ===\n")

for item in data["items"][:5]:
    info = item["volumeInfo"]

    title = info.get("title", "Нет названия")
    authors = info.get("authors", ["Нет автора"])
    published = info.get("publishedDate", "Нет даты")

    print("Название:", title)
    print("Автор:", ", ".join(authors))
    print("Дата:", published)
    print("-" * 30)
