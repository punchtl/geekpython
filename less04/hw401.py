from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Введи время работы: "))
    rate = int(input("Ставка в час: "))
    prize = int(input("Премия: "))
    print((time_work * rate) + prize)