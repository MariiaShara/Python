from abc import ABC, abstractmethod

class Warehouse:
    equipment = {}

    def __str__(self):
        return f"Equipment at warehouse {str(Warehouse.equipment)}."

    def eq_received(self, *args):
        try:
            for item in args:
                item.quantity1 = int(input(f"Enter quantity of {item.model} to be received: "))
                if item.model in Warehouse.equipment:
                    item.quantity = Warehouse.equipment.get(item.model, {}).get("quantity", "") + item.quantity1
                else:
                    item.quantity = item.quantity1
                Warehouse.equipment[item.model] = {"price": item._price,
                                                       "quantity": item.quantity}
        except:
            return f"Wrong data."
        
    def eq_shipped(self, *args):
        try:
            for item in args:
                item.quantity2 = int(input(f"Enter quantity of {item.model} to be shipped: "))
                if item.model in Warehouse.equipment:
                    if item.quantity2 <= item.quantity:
                        Warehouse.equipment[item.model] = {"price": item._price, "quantity": item.quantity - item.quantity2}
                    else:
                        print ("There is not enough of such equipment at the warehouse.")
                else:
                    print ("There is no such equipment at the warehouse.")
        except:
            return f"Wrong data."

    def get_quantity(self, item):
        try:
            return f"Quantity of {item.model}: {Warehouse.equipment.get(item.model, {}).get('quantity', '')}."
        except:
            return f"Wrong data."

class OfficeEquipment(ABC):
    """Common base class for all office equipment."""
    
    def __init__(self, model, price):
        self.model = model
        self._price = price
        self.is_broken = False

    def __str__(self):
        return f"Equipment model: {self.model}, price: {self._price}."

    @abstractmethod
    def is_working(self):
        pass

    @staticmethod
    def get_info():
        print ("Info about the class: this is office equipment.")


class Printer(OfficeEquipment):
    type_of_equipment = "Printer"

    def __init__(self, model, price):
        super().__init__(model, price)

    @classmethod
    def get_type_of_equipment(cls):
        return f"This is {cls.type_of_equipment}."

    def is_working(self):
        return f"{self.model} is printing."


class Scanner(OfficeEquipment):
    type_of_equipment = "Scanner"

    def __init__(self, model, price):
        super().__init__(model, price)

    @classmethod
    def get_type_of_equipment(cls):
        return f"This is {cls.type_of_equipment}."

    def is_working(self):
        return f"{self.model} is scanning."


class Copier(OfficeEquipment):
    type_of_equipment = "Copier"

    def __init__(self, model, price):
        super().__init__(model, price)
        self.needs_refill = False

    @classmethod
    def get_type_of_equipment(cls):
        return f"This is {cls.type_of_equipment}."

    def is_working(self):
        return f"{self.model} is copying."

p1 = Printer("HP DeskJet 2545", 250)
p2 = Printer("HP OfficeJet Pro 8720", 370)
s1 = Scanner("HP ScanJet Pro 3000", 480)
s2 = Scanner("Epson DS-870", 780)
c1 = Copier("Canon ImageRUNNER C475iFZ", 380)
c2 = Copier("HP Color LaserJet E57540", 450)
print(p1)
print(p2)
print(s1)
print(s2)
print(c1)
print(c2)
print(p1.is_working())
print(c1.is_working())
print(s1.is_working())
print(p1.is_broken)
print(c1.needs_refill)
p1.get_info()
Printer.get_info()
print(p1.get_type_of_equipment())
print(c1.get_type_of_equipment())
print(s1.get_type_of_equipment())
warehouse = Warehouse()
warehouse.eq_received(p1)
warehouse.eq_received(p2)
warehouse.eq_received(s2)
warehouse.eq_received(p2)
print(warehouse)
warehouse.eq_shipped(p1)
warehouse.eq_shipped(c2)
warehouse.eq_shipped(s2, p2)
print(warehouse)
print(warehouse.get_quantity(p2))




