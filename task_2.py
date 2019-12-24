class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self):
        r = 25  # масса асфальта для покрытия одного кв метра дороги толщиной в 1 см
        l = 5  # толщина дорожного полотна в см
        print(
            f"Масса асфальта, необходимого для покрытия дорожного полотна шириной {self._width}м и длиной {self._length}м, равна {round((self._length * self._width * r * l) / 1000)} т.")


road_1 = Road(5000, 20)
road_1.mass_asphalt()
road_2 = Road(10000, 15)
road_2.mass_asphalt()
