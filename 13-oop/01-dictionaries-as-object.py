import json


def speak(self):
    return f"Hi! My name is {self['first_name']} and I have {self['legs']} legs."


person = {
    'first_name': 'Matteo Antony',
    'last_name': 'Mistretta',
    'date_of_birth': '1982-10-17',
    'legs': 2,
    'speak': speak
}

print(person['speak'](person))

another_person = {
    'first_name': 'George',
    'last_name': 'Jetson',
    'date_of_birth': '2022-08-22',
    'legs': 2,
    'speak': speak
}

print(another_person['speak'](another_person))
print(another_person['speak'](person))


del person['speak']
string = json.dumps(person)
print(string)
