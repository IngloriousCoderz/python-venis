class LineItem:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

    def calculate_amount(self):
        return self.quantity * self.price


class Cart:
    def __init__(self, line_items):
        self.line_items = line_items

    def calculate_total(self):
        total = 0
        for line_item in self.line_items:
            total += line_item.calculate_amount()
        return total


apples = LineItem(2, 1)
bananas = LineItem(3, 1.5)
cart = Cart([apples, bananas])
cart.calculate_total()  # ?


def calculate_amount(line_item):
    return line_item.quantity * line_item.price


def calculate_total(line_items):
    total = 0
    for item in line_items:
        total += calculate_amount(item)
    return total


class LineItem:
    pass


apples = LineItem()
apples.quantity = 2
apples.price = 1

bananas = LineItem()
bananas.quantity = 3
bananas.price = 1.5

line_items = [apples, bananas]

calculate_total(line_items)  # ?


class Person:
    pass


person = Person()
person.first_name = 'Matteo Antony'
person.last_name = 'Mistretta'
person.date_of_birth = '1982-10-17'
person  # ?
vars(person)  # ?
