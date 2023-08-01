# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv

class GradeValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not (2 <= value <= 5):
            raise ValueError(f"Invalid grade: {value}. Grades must be between 2 and 5.")
        instance.__dict__[self.name] = value


class TestResultValidator:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name, None)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError(f"Invalid test result: {value}. Test results must be between 0 and 100.")
        instance.__dict__[self.name] = value


class Subject:
    grade = GradeValidator()
    test_result = TestResultValidator()

    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, full_name, subjects_file):
        self.full_name = full_name.title()
        self.subjects = {}
        self.load_subjects_from_csv(subjects_file)

    def load_subjects_from_csv(self, subjects_file):
        with open(subjects_file, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                subject_name = row[0]
                self.subjects[subject_name] = Subject(subject_name)

    def add_grade(self, subject_name, grade):
        if subject_name not in self.subjects:
            raise ValueError(f"Subject {subject_name} is not valid for this student.")
        self.subjects[subject_name].grade = grade

    def add_test_result(self, subject_name, test_result):
        if subject_name not in self.subjects:
            raise ValueError(f"Subject {subject_name} is not valid for this student.")
        self.subjects[subject_name].test_result = test_result

    def get_average_grade(self):
        total_grades = 0
        num_grades = 0
        for subject in self.subjects.values():
            if subject.grade is not None:
                total_grades += subject.grade
                num_grades += 1
        return total_grades / num_grades if num_grades > 0 else 0

    def get_average_test_result(self, subject_name):
        if subject_name not in self.subjects:
            raise ValueError(f"Subject {subject_name} is not valid for this student.")
        subject = self.subjects[subject_name]
        return subject.test_result if subject.test_result is not None else 0


# Пример использования:
subjects_file = "subjects.csv"
student1 = Student("john doe", subjects_file)

student1.add_grade("Math", 4)
student1.add_test_result("Math", 80)

student1.add_grade("Science", 5)
student1.add_test_result("Science", 90)

student1.add_grade("English", 3)
student1.add_test_result("English", 70)

print(f"Student: {student1.full_name}")
for subject_name, subject in student1.subjects.items():
    print(f"{subject_name}: Grade - {subject.grade}, Test Result - {subject.test_result}")

print(f"Average Grade: {student1.get_average_grade()}")
print(f"Average Test Result for Math: {student1.get_average_test_result('Math')}")
