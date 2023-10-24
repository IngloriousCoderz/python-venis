squares = []
for num in range(10):
  squares.append(num**2)

# can be written with lambdas as:
squares = list(map(lambda num: num**2, range(10)))

# or, using a named function:
square = lambda num: num**2
squares = list(map(square, range(10)))

# or with list comprehensions:
squares = [num**2 for num in range(10)]

evens = [num for num in range(10) if num % 2 == 0] # filter with an 'if'
