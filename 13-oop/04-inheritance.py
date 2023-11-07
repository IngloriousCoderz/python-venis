class Person:
    legs = 2

    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def speak(self):
        return f"Hi! My name is {self.first_name} and I have {self.legs} legs."

    def pay_taxes(self):
        return "(Crying in Italian)"


class Dog(Person):
    legs = 4

    def speak(self):
        message = super().speak()
        [_, rest] = message.split('! ')
        return f"Woof! {rest}"

    def bark(self):
        return "Bark!"

    __bark = bark


dog = Dog('Arya', 'Mistretta', '2014-12-10')
dog.speak()  # ?
dog.bark()  # ?
dog.legs  # ?
dog.pay_taxes()  # ?
dog._Dog__bark  # ?


class Animal:
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


class Human(Mammal):
    pass
