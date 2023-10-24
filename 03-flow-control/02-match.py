# match is pretty much like a switch
status = int(input('Server status: '))

if status == 200 or status == 201 or status == 204:
  print('Ok')
elif status == 404:
  print('Not Found')
elif status == 500:
  print('Internal Server Error')
else:
  print('Status not recognized:', status)

match status:
  case 200 | 201 | 204:
    print('Ok')
  case 404:
    print('Not Found')
  case 500:
    print('Internal Server Error')
  case _:
    print('Status not recognized:', status)

# match can also extract components
point = [4, 2, 3]

match point:
  case [0, 0]:
    print('Origin')
  case [0, y]:
    print(f"Lies on the y axis, Y={y}")
  case [x, 0]:
    print(f"Lies on the x axis, X={x}")
  case [x, y] if x == y: # guard: an if clause inside of a case!
    print(f"Lies on a diagonal, X=Y={x}")
  case [x, y]:
    print(f"X={x}, Y={y}")
  case _:
    print('Not a point')

# For other features of match @see https://docs.python.org/3/tutorial/controlflow.html#match-statements
