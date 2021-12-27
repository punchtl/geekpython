from itertools import count
from itertools import cycle


def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def my_cycle_func(new_list, iteration):
    i = 0
    iter = cycle(new_list)
    while i < iteration:
        print(next(iter))
        i += 1


my_count_func(start_number=int(input("Начальное число: ")), stop_number=int(input("Конечное число: ")))
my_cycle_func(new_list=[1, 2, 3, 4, 5], iteration=int(input("Введи количество повторений: ")))
