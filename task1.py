def div_func(div_1, div_2):
    quat = round((div_1 / div_2), 2)
    return quat


while True:
    div_1 = input("Enter the dividend number: ")
    div_2 = input("Enter the divisor number: ")
    try:
        div_1 = float(div_1)
        div_2 = float(div_2)
        div_func(div_1, div_2)
        break
    except ValueError:
        print("You should enter a number!")
    except ZeroDivisionError:
        print("You can't divide by zero")

print(f"The quotient is {div_func(div_1, div_2)}")
