def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Ivanov', name='Ivan', year='2000', city='Moscow', email='mail@mail.ru',
              telephone='8-888-888-88-88'))