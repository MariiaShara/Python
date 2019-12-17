my_list = [2, 6, 4, 8, 3, 22]
new_list = [el for i, el in enumerate(my_list) if my_list[i] > my_list[i - 1]]
print(my_list)
print(new_list)
