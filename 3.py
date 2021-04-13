# Реализовать функцию my_func(), которая принимает три позиционных
# аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(argum1 , argum2, argum3):
    if argum1 >= argum3 and argum2 >= argum3:
        return argum1 + argum2
    elif argum1 > argum2 and argum1 < argum3:
        return argum1 + argum3
    else:
        return argum2 + argum3
print(f'Результат сложения двух наибольшийх чисел - {my_func(int(input("введите первый аргумент ")), int(input("введите следующий аргумент ")), int(input("введите третий аргумент ")))}')