rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
my_text = []
try:
    with open("for_task_4.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            print(line)
            line = line.split("-")
            my_text.append(rus[line[0]] + "-" + line[1] + "\n")

except IOError:
    print("Input Output Error")

try:
    with open("For_task_4_new.txt", "w", encoding="utf-8") as f:
        f.writelines(my_text)

except IOError:
    print("Input Output Error")
