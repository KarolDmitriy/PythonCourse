# Найдите сумму цифр трехзначного числа

number = input("Введите число - ")
summ = 0
for n in range(len(number)):
    summ += int(number[n])

print(summ)