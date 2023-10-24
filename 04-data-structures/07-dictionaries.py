person = {'name': 'Matteo Antony', 'date_of_birth': '1982-10-17', 'eyes': 2}
print(person)

print(person['name'])
person['nose'] = 1
print(person)
person['nose'] = 2
print(person)
del person['nose']
print(person)

print(list(person))
print(sorted(person))
print('name' in person)

print(dict([('name', 'Antony'), ('date_of_birth', '1982-10-17'), ('eyes', 2)]))

print(list(person.items()))

for key in person:
    print(key, person[key])

for key, value in person.items():
    print(key, value)
