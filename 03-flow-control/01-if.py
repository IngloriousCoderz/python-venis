if 2 < 3:
  print('Two is less than three')

if 2 > 1:
  print('Two is greater than one')

if 2 < 3:
  print('Two is less than three')
elif 2 > 1:
  print('Two is greater than one')

number = 42

guess = int(input('Guess my number: '))

if guess < number:
  print('Too low')
elif guess > number:
  print('Too high')
else:
  print('Kudos!')

# shorthand, @see https://www.w3schools.com/python/python_conditions.asp

a = 2
b = 330
print('A') if a > b else print('B')
