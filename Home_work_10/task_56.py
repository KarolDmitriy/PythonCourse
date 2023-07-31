# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

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

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name, age, **kwargs):
        if animal_type == "Fish":
            return Fish(name, age, **kwargs)
        elif animal_type == "Bird":
            return Bird(name, age, **kwargs)
        elif animal_type == "Snake":
            return Snake(name, age, **kwargs)
        else:
            raise ValueError("Неверный тип животного.")

# Пример использования класса-фабрики
fish = AnimalFactory.create_animal("Fish", "Немо", 2, fin_type="Лопатчатые")
bird = AnimalFactory.create_animal("Bird", "Чижик", 1, feather_type="Перья с разноцветными полосками")
snake = AnimalFactory.create_animal("Snake", "Кобра", 5, venom_type="Нейротоксин")

fish.show_info()
bird.show_info()
snake.show_info()


