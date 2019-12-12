def my_func(val_1, val_2, val_3):
    val_1 = float(val_1)
    val_2 = float(val_2)
    val_3 = float(val_3)
    if min(val_1, val_2, val_3) == val_1:
        return val_2 + val_3
    elif min(val_1, val_2, val_3) == val_2:
        return val_1 + val_3
    else:
        return val_1 + val_2


while True:
    val_1 = input("Enter the first number: ")
    val_2 = input("Enter the second number: ")
    val_3 = input("Enter the third number: ")
    try:
        val_1 = float(val_1)
        val_2 = float(val_2)
        val_3 = float(val_3)
        my_func(val_1, val_2, val_3)
        break
    except ValueError:
        print("You should enter a number!")

print(f"The sum of two biggest numbers is: {my_func(val_1, val_2, val_3)}.")
