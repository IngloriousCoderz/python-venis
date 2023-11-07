def create_person(first_name, last_name, date_of_birth):
    def speak(self):
        return f"Hi! My name is {self['first_name']} and I have {self['legs']} legs."

    return {
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
        'legs': 2,
        'speak': speak
    }


person = create_person('Matteo Antony', 'Mistretta', '1982-10-17')
print(person['speak'](person))

another_person = create_person('George', 'Jetson', '2022-08-22')
print(another_person['speak'](another_person))
print(another_person['speak'](person))
