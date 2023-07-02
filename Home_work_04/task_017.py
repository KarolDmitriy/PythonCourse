# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

def calculate_withdrawal_fee(amount):
    fee = amount * 0.015
    fee = max(fee, 30)  # Минимальная комиссия - 30 у.е.
    fee = min(fee, 600)  # Максимальная комиссия - 600 у.е.
    return fee


def calculate_interest(amount):
    return amount * 0.03


def calculate_wealth_tax(amount):
    return amount * 0.1


def display_balance(balance):
    print(f"Текущий баланс: {round(balance, 2)} у.е.")


def deposit(balance, amount):
    if amount % 50 != 0:
        print("Сумма пополнения должна быть кратной 50")
        return balance

    balance += amount

    return balance


def withdraw(balance, amount):
    if amount % 50 != 0:
        print("Сумма снятия должна быть кратной 50")
        return balance

    if amount > balance:
        print("Сумма снятия превышает баланс")
        return balance

    withdrawal_fee = calculate_withdrawal_fee(amount)
    balance -= amount + withdrawal_fee

    return balance


def atm():
    balance = 0
    operations_count = 0
    transactions = []

    while True:
        print("Выберите действие: ")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")
        choice = input("Ваш выбор: ")

        if choice == "1":  # Пополнение
            amount = int(input("Введите сумму пополнения (кратную 50): "))
            balance = deposit(balance, amount)
            operations_count += 1

            if operations_count % 3 == 0:
                interest = calculate_interest(balance)
                balance += interest

            if balance > 5000000:
                wealth_tax = calculate_wealth_tax(balance)
                balance -= wealth_tax

            transactions.append(f"Пополнение: +{amount} у.е.")

        elif choice == "2":  # Снятие
            amount = int(input("Введите сумму снятия (кратную 50): "))
            balance = withdraw(balance, amount)
            operations_count += 1

            if operations_count % 3 == 0:
                interest = calculate_interest(balance)
                balance += interest

            if balance > 5000000:
                wealth_tax = calculate_wealth_tax(balance)
                balance -= wealth_tax

            transactions.append(f"Снятие: -{amount} у.е.")

        elif choice == "3":  # Выход
            break

        display_balance(balance)

    print("Операции:")
    for transaction in transactions:
        print(transaction)


# Запуск программы
atm()
