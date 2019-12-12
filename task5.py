sum = 0
try:
    while True:
        user_numbers = input(
            "Enter numbers using space key to separate them,\npress ENTER to get the sum of the numbers or any symbol to exit:")
        for number in map(int, user_numbers.split()):
            sum += number
        print(f"The sum of your numbers is {sum}.")
except ValueError:
    if sum != 0:
        print(f"The sum of your numbers is {sum}.")