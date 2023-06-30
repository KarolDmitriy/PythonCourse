# Напишите программу банкомат.
# Начальная сумма равна нулю.
# Допустимые действия: пополнить, снять, выйти.
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте.
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной.
# Любое действие выводит сумму денег.

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


def atm():
    balance = 0
    operations_count = 0

    while True:
        print("Выберите действие: ")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")
        choice = input("Ваш выбор: ")

        if choice == "1":  # Пополнение
            amount = int(input("Введите сумму пополнения (кратную 50): "))
            if amount % 50 != 0:
                print("Сумма пополнения должна быть кратной 50")
                continue

            balance += amount
            operations_count += 1

            if operations_count % 3 == 0:
                interest = calculate_interest(balance)
                balance += interest

            if balance > 5000000:
                wealth_tax = calculate_wealth_tax(balance)
                balance -= wealth_tax

        elif choice == "2":  # Снятие
            amount = int(input("Введите сумму снятия (кратную 50): "))
            if amount % 50 != 0:
                print("Сумма снятия должна быть кратной 50")
                continue

            if amount > balance:
                print("Сумма снятия превышает баланс")
                continue

            operations_count += 1

            if operations_count % 3 == 0:
                interest = calculate_interest(balance)
                balance += interest

            withdrawal_fee = calculate_withdrawal_fee(amount)
            balance -= amount + withdrawal_fee

            if balance > 5000000:
                wealth_tax = calculate_wealth_tax(balance)
                balance -= wealth_tax

        elif choice == "3":  # Выход
            break

        display_balance(balance)


# Запуск программы
atm()
