class Person:
    legs = 2

    def __init__(self, first_name, last_name, date_of_birth):
        # self.legs = 2
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def speak(self):
        return f"Hi! My name is {self.first_name} and I have {self.legs} legs."

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


person = Person('Matteo Antony', 'Mistretta', '1982-10-17')
print(person)
print(person.__str__())
print(person.__repr__())
print(vars(person))
print(person.legs)
print(person.first_name)

print(person.speak())

another_person = Person('George', 'Jetson', '2022-08-22')
print(another_person.speak())

print(another_person.legs)
print(Person.legs)
# print(Person.first_name)
print(another_person.speak)
print(Person.speak)
print(Person.speak(another_person))
