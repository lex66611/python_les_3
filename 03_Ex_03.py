def my_func(a, b, c):
    items = [a, b, c]
    items.remove(min(items))

    return sum(items)


a, b, c = int(input("Введите число a: ")), int(input("Введите число b: ")), int(input("Введите число c: "))

print(my_func(a, b, c))
