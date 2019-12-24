class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name + " " + self.surname)

    def get_total_income(self):
        print(sum(self._income.values()))


a = Position("Михаил", "Иванов", "Бухгалтер", 65000, 20000)
b = Position("Сергей", "Петров", "Инженер", 98000, 40000)
c = Position("Александр", "Бубнов", "Рабочий", 35000, 10000)
a.get_full_name()
a.get_total_income()
b.get_full_name()
b.get_total_income()
c.get_full_name()
c.get_total_income()
