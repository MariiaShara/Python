from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size=None, height=None):
        self.name = name
        self.size = size
        self.height = height

    @abstractmethod
    def fabric_use(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def fabric_use(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def fabric_use(self):
        return 2 * self.height + 0.3


coat_1 = Coat("coat", 5)
print(f"Fabric needed to sew a {coat_1.name} size {coat_1.size}: {coat_1.fabric_use:.2f}.")

suit_1 = Suit("suit", 6)
print(f"Fabric needed to sew a {suit_1.name} with height {suit_1.height} : {suit_1.fabric_use:.2f}.")

print(
    f"Fabric needed to sew a {coat_1.name} and a {suit_1.name}: {(coat_1.fabric_use + suit_1.fabric_use):.2f} all together.")
