class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}.")

    def show_speed(self):
        print(f"Машина {self.name} едет со скоростью {self.speed}.")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} едет с превышением скорости.")
        else:
            print(f"Машина {self.name} едет со скоростью {self.speed}.")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} едет с превышением скорости.")
        else:
            print(f"Машина {self.name} едет со скоростью {self.speed}.")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


car_1 = TownCar(70, "Черный", "Ford")
car_2 = SportCar(100, "Серебристый", "Mazda")
car_3 = WorkCar(35, "Белый", "Toyota")
car_4 = PoliceCar(50, "Синий", "Crysler")

print(car_1.speed)
print(car_2.color)
print(car_3.name)
print(car_4.is_police)

car_1.go()
car_2.stop()
car_3.turn("направо")
car_4.turn("налево")
car_1.show_speed()
car_2.show_speed()
car_3.show_speed()
car_4.show_speed()
