def int_func(inp_word: str):
    return "".join([
        inp_word[0].upper(), inp_word[1:]
    ])
words = input("Введите строку из нескольких слов: ").split()

words = [int_func(x) for x in words]

print(" ".join(words))