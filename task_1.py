# вариант 1
from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый", "Желтый"]

    def running(self):
        print(TrafficLight.__color[0])
        sleep(7)
        print(TrafficLight.__color[1])
        sleep(2)
        print(TrafficLight.__color[2])
        sleep(10)
        print(TrafficLight.__color[3])
        sleep(1)


TrafficLight = TrafficLight()
while True:
    TrafficLight.running()

# вариант 2
from time import sleep


class TrafficLight:
    __color = ["Красный", "Желтый", "Зеленый", "Желтый"]

    def running(self):

        for i in range(len(TrafficLight.__color)):
            print(TrafficLight.__color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(10)
            elif i == 3:
                sleep(1)


TrafficLight = TrafficLight()
while True:
    TrafficLight.running()
