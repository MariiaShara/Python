my_num = [7, 5, 3, 3, 2]
print(my_num)
user_num = int(input("Please, enter a digit: "))
if user_num >= 0 and user_num <= 9:
    my_num.reverse()
    if user_num <= max(my_num):
        for el in my_num:
            if el >= user_num:
                my_num.insert(my_num.index(el), user_num)
                break
    else:
        my_num.append(user_num)
    my_num.reverse()
    print(my_num)
else:
    print("You shoud have entered a numeral from 0 to 9.")