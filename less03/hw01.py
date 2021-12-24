def my_func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "На ноль делить нельзя"
    except ValueError:
        return "Вводи только числа"


print(my_func(int(input("Введи первое число = ")), int(input("Введи второе число = "))))
