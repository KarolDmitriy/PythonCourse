import os

def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                surname, name, patronymic, phone_number = line.strip().split(',')
                contacts.append({'surname': surname, 'name': name, 'patronymic': patronymic, 'phone_number': phone_number})
    return contacts

def save_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['surname']},{contact['name']},{contact['patronymic']},{contact['phone_number']}\n")

def search_contacts(contacts, search_term):
    results = []
    for contact in contacts:
        if search_term.lower() in contact['surname'].lower() or search_term.lower() in contact['name'].lower():
            results.append(contact)
    return results

def add_contact(contacts):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    contacts.append({'surname': surname, 'name': name, 'patronymic': patronymic, 'phone_number': phone_number})
    print("Контакт успешно добавлен!")

def edit_contact(contact):
    print("Выберите поле для редактирования:")
    print("1. Фамилия")
    print("2. Имя")
    print("3. Отчество")
    print("4. Номер телефона")
    field = int(input("Введите номер поля: "))
    if field == 1:
        contact['surname'] = input("Введите новую фамилию: ")
    elif field == 2:
        contact['name'] = input("Введите новое имя: ")
    elif field == 3:
        contact['patronymic'] = input("Введите новое отчество: ")
    elif field == 4:
        contact['phone_number'] = input("Введите новый номер телефона: ")
    else:
        print("Некорректный выбор!")
        return
    print("Контакт успешно отредактирован!")

def delete_contact(contacts, contact):
    contacts.remove(contact)
    print("Контакт успешно удален!")

def main():
    # Получение текущей директории
    current_directory = os.getcwd()
    # Создание пути к файлу на уровень ниже. К исполняемому файлу.
    filename = os.path.join(current_directory, 'Home_Work_008', 'contacts.txt')
    contacts = load_contacts(filename)
    while True:
        print("1. Вывести все контакты")
        print("2. Поиск контактов")
        print("3. Добавить контакт")
        print("4. Редактировать контакт")
        print("5. Удалить контакт")
        print("6. Сохранить и выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            print("Список контактов:")
            for contact in contacts:
                print(f"{contact['surname']} {contact['name']} {contact['patronymic']}: {contact['phone_number']}")
        elif choice == '2':
            search_term = input("Введите фамилию или имя для поиска: ")
            search_results = search_contacts(contacts, search_term)
            if search_results:
                print("Результаты поиска:")
                for contact in search_results:
                    print(f"{contact['surname']} {contact['name']} {contact['patronymic']}: {contact['phone_number']}")
            else:
                print("Контакты не найдены.")
        elif choice == '3':
            add_contact(contacts)
        elif choice == '4':
            search_term = input("Введите фамилию или имя для поиска контакта, который нужно отредактировать: ")
            search_results = search_contacts(contacts, search_term)
            if search_results:
                if len(search_results) > 1:
                    print("Найдено несколько контактов. Уточните запрос.")
                else:
                    edit_contact(search_results[0])
            else:
                print("Контакты не найдены.")
        elif choice == '5':
            search_term = input("Введите фамилию или имя для поиска контакта, который нужно удалить: ")
            search_results = search_contacts(contacts, search_term)
            if search_results:
                if len(search_results) > 1:
                    print("Найдено несколько контактов. Уточните запрос.")
                else:
                    delete_contact(contacts, search_results[0])
            else:
                print("Контакты не найдены.")
        elif choice == '6':
            save_contacts(filename, contacts)
            print("Контакты успешно сохранены.")
            break
        else:
            print("Некорректный выбор!")

if __name__ == "__main__":
    main()
