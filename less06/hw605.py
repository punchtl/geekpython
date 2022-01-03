class Stationery:
    atr_title = 'Title'

    def draw(self):
        print('Отрисовка.')


class Pen(Stationery):
    def draw(self):
        print('Ручка')


class Pencil(Stationery):
    def draw(self):
        print('Карандаш')


class Handle(Stationery):
    def draw(self):
        print('Маркер')


my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()
