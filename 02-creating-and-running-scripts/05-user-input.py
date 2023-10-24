name = input('What is your name? ')
print(f"Howdy {name}!")

number = int(input('Type a number: '))
print(f'The double of {number} is {number * 2}')

from getpass import getpass
password = getpass('Type a password: ') # optional custom message
print(password)
