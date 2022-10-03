# Напишите программу, которая принимает на вход вещественное число и показывает
# сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

from functools import reduce


def int2(x):
    if str(type(x)) == "<class 'str'>":
        if x >= '0' and x <= '9':
            return int(x)
        return 0
    return x


print(reduce(lambda a, b: int2(a) + int2(b),
      list(input('Введите вещественное число: '))))
