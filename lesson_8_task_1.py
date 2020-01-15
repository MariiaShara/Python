class Date:
    def __init__(self, day_month_year):
        self.day_month_year = day_month_year

    def __str__(self):
        return f"The date is {self.day_month_year}."

    @classmethod
    def get_date(cls, day_month_year):
        date = day_month_year.split("-")
        return {"day": int(date[0]), "month": int(date[1]), "year": int(date[2])}

    @staticmethod
    def validate_date(day, month, year):
        if month < 1 or month > 12 or year < 0 or year > 2020:
            return f"Wrong month and/or year."
        else:
            number_of_days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                number_of_days_in_month[2] = 29
            if day < 1 or day > number_of_days_in_month[month]:
                return f"Wrong day."
            else:
                return f"Correct date."


date_1 = Date("12-5-2019")
print(date_1)
print(Date.get_date('12-5-2019'))
print(date_1.get_date('12-5-2019'))
print(Date.validate_date(31, 4, 2019))
print(Date.validate_date(29, 2, 2016))
print(date_1.validate_date(12, 14, 2019))
