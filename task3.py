months_dict = {1 : "winter", 2 : "winter", 3 : "spring", 4 : "spring", 5 : "spring", 6 : "summer", 7 : "summer", 8 : "summer", 9 : "fall", 10 : "fall", 11 : "fall", 12 : "winter"}
month = int(input("Enter the month's number: "))
if month >= 1 and month <= 12:
    season = months_dict.get(month)
    print("It's " + str(season) + ".")
elif month <= 0:
    print("Month's number can't be less than 1.")
elif month > 12:
    print("There are only 12 months in a year.")


winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
fall = [9, 10, 11]
month = int(input("Enter the month's number: "))
if month >= 1 and month <= 12:
    if month in winter:
        print("It's winter.")
    if month in spring:
        print("It's spring.")
    if month in summer:
        print("It's summer.")
    if month in fall:
        print("It's fall.")
elif month <= 0:
    print("Month's number can't be less than 1.")
elif month > 12:
    print("There are only 12 months in a year.")



