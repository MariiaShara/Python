employees = []

try:
    with open("for_task_3.txt") as f:
        for line in f:
            line = line.split()
            employees.append(line)

    my_dict = dict(employees)
    salary = []
    print(f"Сотрудники с окладом менее 20000:")
    for keys in my_dict:
        if int(my_dict.get(keys)) < 20000:
            print(keys)
        salary.append(int(my_dict.get(keys)))
    average_salary = sum(salary) / len(salary)
    print(f"Средняя выличина дохода сотрудников: {round(average_salary)}")

except IOError:
    print("Ошибка ввода-вывода ")

except ValueError:
    print("В файле содержатся неправильные данные.")