import json

person = {'name': 'Matteo Antony',
          'date_of_birth': '1982-10-17', 'legs': ['left', 'right']}

string = json.dumps(person)
print(repr(string))

person = json.loads(string)
print(person)

with open('db.json', 'w', encoding="utf-8") as f:
    json.dump(person, f)

with open('db.json', 'r', encoding="utf-8") as f:
    person = json.load(f)
    print(person)
