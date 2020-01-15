class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Комплексное число {self.a} + {self.b} * j."

    def __add__(self, other):
        return f"Сумма комплексных чисел равна: {self.a + other.a} + {self.b + other.b} * j."

    def __mul__(self, other):
        return f"Произведение комплексных чисел равно: {(self.a * other.a) - (self.b * other.b)} + {(self.b * other.a) + (self.a * other.b)} * j."


complex_number_1 = ComplexNumber(2, 5)
complex_number_2 = ComplexNumber(7, 9)
print(complex_number_1)
print(complex_number_2)
print(complex_number_1 + complex_number_2)
print(complex_number_1 * complex_number_2)
