from itertools import count

n = int(input("Введите число, с которого начать генерировать целые числа: "))
for el in count(n):
    print(el)

from itertools import cycle

for el in cycle([2, 56, 4, 89, 67]):
    print(el)
