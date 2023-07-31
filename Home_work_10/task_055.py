# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")

class Fish(Animal):
    def __init__(self, name, age, fin_type):
        super().__init__(name, age)
        self.fin_type = fin_type

    def show_info(self):
        super().show_info()
        print(f"Тип плавников: {self.fin_type}")
        print("------------")

class Bird(Animal):
    def __init__(self, name, age, feather_type):
        super().__init__(name, age)
        self.feather_type = feather_type

    def show_info(self):
        super().show_info()
        print(f"Тип перьев: {self.feather_type}")
        print("------------")

class Snake(Animal):
    def __init__(self, name, age, venom_type):
        super().__init__(name, age)
        self.venom_type = venom_type

    def show_info(self):
        super().show_info()
        print(f"Тип яда: {self.venom_type}")
        print("------------")

# Пример использования классов
fish = Fish("Немо", 2, "Лопатчатые")
bird = Bird("Чижик", 1, "Перья с разноцветными полосками")
snake = Snake("Кобра", 5, "Нейротоксин")

fish.show_info()
bird.show_info()
snake.show_info()
