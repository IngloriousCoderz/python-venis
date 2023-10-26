import re

matches = re.findall(
    r'^[\w\.]+@\w+\.\w{2,4}$', 'antony.mistretta@gmail.com')
print(matches)

result = re.sub(r'\sand\s', ' & ', 'Monsters And Co.', flags=re.IGNORECASE)
print(result)

print('JavaScript is awesome!'.replace('JavaScript', 'Python'))
print('Monsters And Co.'.replace('And', '&'))
print('Andalusia And Co.'.replace('And', '&'))
print('Andalusia And Co.'.replace(' And ', ' & '))
