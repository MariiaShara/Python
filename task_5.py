class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Отрисовка ручкой {self.title}.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Отрисовка карандашом {self.title}.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Отрисовка маркером {self.title}.")


pen_1 = Pen("Erich krause")
pen_2 = Pen("Pilot")
pencil_1 = Pencil("Faber-Castell")
pencil_2 = Pencil("Koh-I-Noor")
handle_1 = Handle("Sharpie")
handle_2 = Handle("Crayola")

pen_1.draw()
pen_2.draw()
pencil_1.draw()
pencil_2.draw()
handle_1.draw()
handle_2.draw()
