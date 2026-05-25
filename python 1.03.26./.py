class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.__position = position

    def get_position(self):
        return self.__position

    def show_info(self):
        print("Имя:", self.get_name())
        print("Возраст:", self.get_age())
        print("Должность:", self.__position)


class Manager(Employee):
    def __init__(self, name, age, position):
        super().__init__(name, age, position)
        self.__team = []

    def add_employee(self, employee):
        if employee not in self.__team:
            self.__team.append(employee)
            print("Сотрудник добавлен в команду")
        else:
            print("Этот сотрудник уже в команде")

    def show_team(self):
        print("Команда менеджера", self.get_name())

        if len(self.__team) == 0:
            print("Команда пустая")
        else:
            for employee in self.__team:
                print("-", employee.get_name())


employees = []


while True:
    print("\n1 - Добавить сотрудника")
    print("2 - Назначить сотрудника менеджеру")
    print("3 - Показать всех сотрудников")
    print("exit - Выход")

    command = input("Введите команду: ")

    if command == "1":
        try:
            name = input("Введите имя: ")
            age = int(input("Введите возраст: "))
            position = input("Введите должность: ")

            manager_check = input("Это менеджер? (да/нет): ")

            if manager_check == "да":
                employee = Manager(name, age, position)
            else:
                employee = Employee(name, age, position)

            employees.append(employee)

            print("Сотрудник успешно добавлен")

        except:
            print("Ошибка ввода данных")

    elif command == "2":
        manager_name = input("Введите имя менеджера: ")
        employee_name = input("Введите имя сотрудника: ")

        manager = None
        worker = None

        for emp in employees:
            if emp.get_name() == manager_name and isinstance(emp, Manager):
                manager = emp

            if emp.get_name() == employee_name:
                worker = emp

        if manager and worker:
            if manager == worker:
                print("Нельзя добавить менеджера самому себе")
            else:
                manager.add_employee(worker)
        else:
            print("Менеджер или сотрудник не найден")

    elif command == "3":
        if len(employees) == 0:
            print("Список сотрудников пуст")
        else:
            for emp in employees:
                print("\n----------------")
                emp.show_info()

                if isinstance(emp, Manager):
                    emp.show_team()

    elif command == "exit":
        print("Программа завершена")
        break

    else:
        print("Неизвестная команда")
