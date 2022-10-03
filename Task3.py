# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму

from functools import reduce
a = int(input('Введите число N => '))
print(list(map(lambda n: (1+1/n)**n, range(1, a+1))))
