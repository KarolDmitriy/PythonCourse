# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name, age, fin_type):
        self.name = name
        self.age = age
        self.fin_type = fin_type

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Тип плавников: {self.fin_type}")
        print("------------")

class Bird:
    def __init__(self, name, age, feather_type):
        self.name = name
        self.age = age
        self.feather_type = feather_type

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Тип перьев: {self.feather_type}")
        print("------------")

class Snake:
    def __init__(self, name, age, venom_type):
        self.name = name
        self.age = age
        self.venom_type = venom_type

    def show_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Тип яда: {self.venom_type}")
        print("------------")

# Пример использования классов
fish = Fish("Немо", 2, "Лопатчатые")
bird = Bird("Чижик", 1, "Перья с разноцветными полосками")
snake = Snake("Кобра", 5, "Нейротоксин")

fish.show_info()
bird.show_info()
snake.show_info()
