# Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N

from functools import reduce
a = int(input('Введите число N => '))
print(list(map(lambda x: reduce(lambda a, b: a * b, range(1, x+1)), range(1, a+1))))
