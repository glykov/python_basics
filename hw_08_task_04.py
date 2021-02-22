# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class WarehouseError(Exception):
    def __init__(self, text):
        self.text = text


class ItemNotFoundError(WarehouseError):
    pass


class Warehouse():
    items = {
        "Printer": [],
        "Scanner": [],
        "Copier": []
    }

    def add_item(self, item):
        if isinstance(item, Printer):
            self.items["Printer"].append(item)
        elif isinstance(item, Scanner):
            self.items["Scanner"].append(item)
        elif isinstance(item, Copier):
            self.items["Copier"].append(item)

    def remove_item(self, item):
        try:
            self.items[item.eq_type].remove(self.find_item(item))
            print(f"{item} is removed")
        except ItemNotFoundError as e:
            print(e.text)

    def find_item(self, item):
        for element in self.items[item.eq_type]:
            if element.manufecturer == item.manufecturer and element.model == item.model:
                return element
        raise ItemNotFoundError("item is not found")

    def count_items(self, item_type):
        return len(self.items[item_type])


class OfficeEquipment():
    def __init__(self, eq_type, manufecturer, model, price=0):
        self.eq_type = eq_type
        self.manufecturer = manufecturer
        self.model = model
        self.price = price

    def __repr__(self):
        return f'{self.eq_type}: {self.manufecturer} {self.model}, ${self.price}'


class Printer(OfficeEquipment):
    def __init__(self, manufecturer, model, price=0, color=False, print_speed=0, number_pages=0):
        super().__init__("printer", manufecturer, model, price)
        self.color = color
        self.print_speed = print_speed
        self.number_pages = number_pages


class Scanner(OfficeEquipment):
    def __init__(self, manufecturer, model, price=0, scan_speed=0):
        super().__init__("scanner", manufecturer, model, price)
        self.scan_speed = scan_speed


class Copier(OfficeEquipment):
    def __init__(self, manufecturer, model, price=0, color=False, scan_speed=0, print_speed=0, number_pages=0):
        super().__init__("copier", manufecturer, model, price)
        self.color = color
        self.scan_speed = scan_speed
        self.print_speed = print_speed
        self.number_pages = number_pages


if __name__ == '__main__':
    printer = Printer("HP", "Laser 107wr", 7000, False)
    scanner = Scanner("Cannon", "CanoScan LiDE 300", 5250)
    copier_01 = Copier("Xerox", "WorkCenter 3025V_BI", 13000)
    copier_02 = Copier("HP", "LaserJet Pro M132a", 14300)

    wh = Warehouse()
    wh.add_item(printer)
    wh.add_item(scanner)
    wh.add_item(copier_01)
    wh.add_item(copier_02)

    print("We have following items on stock:")
    for i, j in enumerate(wh.items.items(), 1):
        print(i, j[1])
