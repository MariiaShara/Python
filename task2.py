def user_data(name, surname, dob, city, email, phone):
    return ' '.join([name, surname, dob, city, email, phone])


name = input("Enter your first name: ")
surname = input("Enter your last name: ")
dob = input("Enter your date of birth: ")
city = input("Enter your city of residence: ")
email = input("Enter your email address: ")
phone = input("Enter your phone number: ")

print(f"Your data are: {user_data(name, surname, dob, city, email, phone)}.")
