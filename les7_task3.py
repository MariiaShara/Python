class Cell:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        if self.quantity - other.quantity > 0:
            return self.quantity - other.quantity
        else:
            print("Разность количества ячеек двух клеток меньше нуля.")

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, quantity_in_row):
        result = " "
        for i in range(self.quantity // quantity_in_row):
            result += f"{'*' * quantity_in_row} \\n"
        result += f"{'*' * (self.quantity % quantity_in_row)}"
        return result


cell_1 = Cell(11)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
print(cell_2.make_order(3))