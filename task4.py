def my_func(x, y):
    y = abs(y)
    if y == 1:
        return 1 / x
    else:
        return my_func(x, y - 1) * (1 / x)


while True:
    x = input("Enter a positive real number x: ")
    y = input("Enter a negative integer y: ")
    try:
        x = int(x)
        y = int(y)
        if x <= 0 or y >= 0:
            print("Incorrect numbers provided")
        else:
            my_func(x, y)
            break
    except ValueError:
        print("You should enter numbers!")
print(f"{x} raised to the power of {y} is {my_func(x, y)}")
