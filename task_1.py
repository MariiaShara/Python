from sys import argv

script_name, hours_worked, salary_per_hour, bonus = argv


def salary_calc():
    salary = int(hours_worked) * int(salary_per_hour) + int(bonus)
    return salary


print(f"Заработная плата составила: {salary_calc()} руб.")
