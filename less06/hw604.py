class Car:

    def __init__(self, speed, color, name, is_police):
        try:
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = bool(is_police)

        except BaseException:
            return "Error. Please, enter data."
            exit(-1)

    def go(self):
        return "Go."

    def stop(self):
        return "Stop."

    def turn_left(self):
        return "Turn left."

    def turn_right(self):
        return "Turn right."

    def show_speed(self):
        print("Machine normal speed.")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return "Over speed."
        else:
            return "Normal speed"


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return "Over speed."
        else:
            return "Normal speed"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


car1 = SportCar(100, 'Red', 'Toyota', False)
car2 = TownCar(30, 'White', 'Mazda', True)
car3 = WorkCar(70, 'Rose', 'Suzuki', False)
car4 = PoliceCar(110, 'Blue',  'Honda', True)


print(car1.turn_left())
print(car2.turn_right())
print(car3.stop())
print(car4.go())
print(car3.is_police)
print(car4.is_police)
print(car3.show_speed())
print(car4.show_speed())