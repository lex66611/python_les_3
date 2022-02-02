total = 0

while True:
    num = input("Введите строку из чисел через пробел: ").split()
    spec_sym = False

    for number in num:
        if number.isdigit():
            total += int(number)
        else:
            spec_sym = True
            break

    print(f"Общая сумма чисел = {total}")

    if spec_sym:
        break
