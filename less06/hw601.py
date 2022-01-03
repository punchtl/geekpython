import time


def running():
    i = 0
    while i < 5:
        for el in TrafficLight._colors:
            print(el)
            i += 1
            time.sleep(1)


class TrafficLight:
    _color = None
    _colors = ['Красный', 'Желтый', 'Зеленый']

    def __init__(self):
        self._color = self._colors[0]


traffic = TrafficLight()
running()
