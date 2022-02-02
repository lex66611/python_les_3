def my_func(x, y):
    # решение через оператор
    # return x ** y

    # решение через цикл
    chislo = x

    if y > 0:
        for _ in range(1, y):
            chislo *= x
    else:
        for _ in range(1, y, -1):
            chislo /= x

    return chislo


x, y = float(input("Введите число x: ")), int(input("Введите число y: "))

print(my_func(x, y))
