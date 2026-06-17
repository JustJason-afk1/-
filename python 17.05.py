import requests

url = "https://api.le-systeme-solaire.net/rest/bodies/"

response = requests.get(url)
data = response.json()

print("=== ПЛАНЕТЫ СОЛНЕЧНОЙ СИСТЕМЫ ===\n")

for body in data["bodies"]:
    if body["isPlanet"]:

        name = body.get("englishName", "Нет названия")
        gravity = body.get("gravity", "нет данных")
        mass = body.get("mass", {}).get("massValue", "нет данных")
        density = body.get("density", "нет данных")

        print("Планета:", name)
        print("Гравитация:", gravity)
        print("Масса:", mass)
        print("Плотность:", density)
        print("-" * 30)
