name = input("Enter your first name: ")
surname = input("Enter your last name: ")
age = input("Enter your age: ")
city = input("Enter your city of residence: ")
state = input("Enter your state of residence: ")
country = input("Enter your country of residence: ")
postal_code = input("Enter your postal code: ")
my_list = [name, surname, age, city, state, country, postal_code]
print(my_list)
for el in range(len(my_list)-1):
    if el % 2 == 0:
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
print(my_list)


list_1 = input("Enter several numbers or letters, using space key between them: ")
my_list = list_1.split(" ")
print(my_list)
for el in range(len(my_list)-1):
    if el % 2 == 0:
        my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
print(my_list)

