class DivisionByZero(Exception):
    def __init__(self, text):
        self.text = text

dividend = input("Введите делимое: ")
divisor = input("ВВедите делитель: ")

try:
    dividend = int(dividend)
    divisor = int(divisor)
    if divisor == 0:
        raise DivisionByZero("На ноль делить нельзя!")

except ValueError:
    print("Вы ввели не число!")

except DivisionByZero as err:
    print(err)

else:
    quotient = dividend / divisor
    print(f"Все хорошо. Результат деления: {quotient:.2f}.")

finally:
    print("Работа завершена.")
