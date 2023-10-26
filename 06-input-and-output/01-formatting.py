name = 'Antony'
language = 'Python'
print(f"My name is {name} and I <3 {language.upper()}!")

print('My name is {} and I <3 {}!'.format('Antony', 'Python'))
print('My name is {1} and I <3 {0}!'.format('Antony', 'Python'))
print('My name is {name} and I <3 {language}!'.format(
    name='Antony', language='Python'))

othree = 0.1 + 0.2
print(othree)
print('{:.1}'.format(othree))
print(float('{:1.1}'.format(othree)))
print('{:.17}'.format(othree))

pi = 22 / 7
print(pi)
print('{:.2f}'.format(pi))

print(str(pi))
print(repr(pi))
print('Hello world!')
print(repr('Hello world!'))

print(f"The approx value of pi is {pi:.2f}")
