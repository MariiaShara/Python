class OwnError(Exception):
    def __init__(self, text):
        self.text = text


numbers = []
while True:
    num = input("Введите число, для выхода нажмите q: ")
    if num == "q":
        print(f"Ваш список чисел: {numbers}.")
        break
    else:
        try:
            if num.isdigit() is False:
                raise OwnError("Вы ввели не число!")
        except OwnError as err:
            print(err)
        else:
            numbers.append(int(num))
