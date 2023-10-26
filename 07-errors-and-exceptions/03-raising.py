def sum(a, b):
    if a is None:
        raise ValueError("You should provide a value for the first parameter")
    if b is None:
        raise ValueError("You should provide a value for the second parameter")
    return a + b


print(sum(41, None))

try:
    raise NameError('What an ugly name!')
except NameError as error:
    print(error)
    raise RuntimeError('Script exploded') from error

try:
    open('myfilez.txt')
except OSError:
    raise RuntimeError from None

try:
    while True:
        print('Hello world!')
except KeyboardInterrupt:
    print('Did you press Ctrl-C?')
    raise
finally:
    print('Goodbye world!')

print('Hello again!')
