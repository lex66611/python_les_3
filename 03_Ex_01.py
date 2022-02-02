def main(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


a = int(input("Введите число a : "))
b = int(input("Введите число b : "))

print(main(a, b))
