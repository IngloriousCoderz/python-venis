# invoking prior to defining leads to an error
# print_sum(2, 3)

def print_sum(a, b):
  print(a + b)

print(print_sum)
print_sum(2, 3)

def sum(a, b):
  return a + b

print(sum(2, 3))

def to_be_implemented(): # use snake case as a naming convention
  pass # use pass as a placeholder

def create_point(x=0, y=0): # default argument values
  return [x, y]

print(create_point(4, 2))
# positional argument
print(create_point(4))
# keyword argument
print(create_point(y=2))
print(create_point(y=-1, x=1))
# positional argument + keyword argument
print(create_point(2, y=3)) # kw args must always follow pos args
# print(create_point(x=2, 3)) # can't put positional arguments after kw arguments

# dynamic positional and keyword arguments
def define_person(name, *arguments, arms, **keywords):
  print(name)
  for arg in arguments:
    print(arg)

  print(arms)
  for kw in keywords:
    print(f"{kw}: {keywords[kw]}")

define_person('Antony', 'JavaScript', 'Python', arms=2, date_of_birth='1982-10-17', eyes=2)

# For extra features of function @see https://docs.python.org/3/tutorial/controlflow.html#special-parameters

# lambdas are small anonymous functions
square = lambda num: num**2
sum = lambda a, b: a + b

# annotations and documentation
def sum(a: float, b:float) -> float:
  """
  Functions are documented with
  multiline strings
  """
  return a + b

print(sum.__doc__)
print(sum.__annotations__)
print(sum('a', 'b')) # it's not static typing, this still works!

# functions can mute code without having to comment it out!
