# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# - шестизначный идентификационный номер
# - уровень доступа вычисляемый как остаток от деления суммы цифр id на семь.

class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def age(self):
        return self._age

class Employee(Person):
    def __init__(self, first_name, last_name, age, employee_id):
        super().__init__(first_name, last_name, age)
        self._employee_id = employee_id

    @property
    def access_level(self):
        return self._employee_id % 7

# Пример использования класса Сотрудник
employee_id = 123456
employee = Employee("John", "Doe", 30, employee_id)

print(f"Полное имя: {employee.full_name()}")
print(f"Возраст: {employee.age}")
print(f"Идентификационный номер: {employee_id}")
print(f"Уровень доступа: {employee.access_level}")

