# Реализуйте алгоритм перемешивания списка

import random


def array_change(array):
    array2 = list()
    while len(array) > 0:
        random_index = random.randint(0, len(array) - 1)
        array2.append(array[random_index])
        del array[random_index]
    return array2


array = list(range(1, 11))
print(array)
array2 = array_change(array)
print(array2)
