from random import randint

numbers = []
for i in range(8):
    numbers.append(str(randint(-10, 10)))
# print(num)

try:
    with open("For_task_5.txt", "w+") as f:
        f.writelines(' '.join(numbers))
        f.seek(0)
        content = f.read()

except IOError:
    print("Input Output Error")

print(f"Сумма чисел в файле равна: {sum(map(int, content.split()))}.")
