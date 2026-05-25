#Задание 1

class Human:
    def __init__(self, name="", birth="", phone="", city="", country="", address=""):
        self.name = name
        self.birth = birth
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        self.name = input("ФИО: ")
        self.birth = input("Дата рождения: ")
        self.phone = input("Телефон: ")
        self.city = input("Город: ")
        self.country = input("Страна: ")
        self.address = input("Адрес: ")

    def show_data(self):
        print("ФИО:", self.name)
        print("Дата рождения:", self.birth)
        print("Телефон:", self.phone)
        print("Город:", self.city)
        print("Страна:", self.country)
        print("Адрес:", self.address)

    def get_name(self):
        return self.name

    def set_phone(self, phone):
        self.phone = phone


person = Human()
person.input_data()
person.show_data()

print(person.get_name())
print(person.get_phone())


#Задание 2

class City:
    def __init__(self, city_name="", region="", country="", people=0, index="", code=""):
        self.city_name = city_name
        self.region = region
        self.country = country
        self.people = people
        self.index = index
        self.code = code

    def input_info(self):
        self.city_name = input("Название города: ")
        self.region = input("Регион: ")
        self.country = input("Страна: ")
        self.people = int(input("Жители: "))
        self.index = input("Индекс: ")
        self.code = input("Код: ")

    def show_info(self):
        print(self.city_name, self.region, self.country)
        print("Население:", self.people)
        print("Индекс:", self.index)
        print("Код:", self.code)

    def get_population(self):
        return self.population


city = City()
city.input_info()
city.show_info()

print(city.get_population())


#Задание 3

class Country:
    def __init__(self, name="", continent="", population=0, code="", capital="", cities=[]):
        self.name = name
        self.continent = continent
        self.population = population
        self.code = code
        self.capital = capital
        self.cities = cities

    def input_country(self):
        self.name = input("Страна: ")
        self.continent = input("Континент: ")
        self.population = int(input("Население: "))
        self.code = input("Код страны: ")
        self.capital = input("Столица: ")

        count = int(input("Сколько городов: "))

        for i in range(count):
            city = input("Город: ")
            self.cities.append(city)

    def show_country(self):
        print("Страна:", self.name)
        print("Континент:", self.continent)
        print("Население:", self.population)
        print("Код:", self.code)
        print("Столица:", self.capital)
        print("Города:", self.cities)

    def get_capital(self):
        return capital


country = Country()
country.input_country()
country.show_country()

print(country.get_capital())
