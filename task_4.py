my_list = [2, 45, 34, 6, 2, 8, 45, 99]
new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_list)
print(new_list)