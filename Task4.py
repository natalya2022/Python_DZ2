# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from functools import reduce

n = int(input('Введите число N => '))
m = list(range(-n, n+1))
array = map(int, input('Введите позиции через пробел: ').split())
print(list(range(-n, n+1)))
print(reduce(lambda sum, a: sum * m[a], array, 1))
