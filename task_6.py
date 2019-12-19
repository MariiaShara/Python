courses = {}
try:
    with open("for_task_6.txt") as f:
        for line in f:
            line = line.replace(".\n", "")
            line = line.replace(":", "")
            line = line.replace("(l)", "")
            line = line.replace("(pr)", "")
            line = line.replace("(lab)", "")
            line = line.replace("-", "0")
            course, lectures, practice, lab = line.split()
            courses[course] = float(lectures) + float(practice) + float(lab)

except IOError:
    print("Input Output Error")

except ValueError:
    print("В файле содержатся неправильные данные.")

print(f"Общее количество занятий по предметам: {courses}.")
