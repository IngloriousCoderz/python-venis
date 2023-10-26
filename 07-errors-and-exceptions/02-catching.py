number = None
while number is None:
    try:
        number = int(input('Please enter a number: '))
    except ValueError:
        print("Oops, that's not a number!")

print('Your number is', number)

try:
    pass
except (RuntimeError, TypeError, NameError):
    pass

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
except FileNotFoundError as err:
    print('File not found:', err)
except ValueError as err:
    print('Could not convert value to int:', err)
except BaseException as err:
    print(f"Unexpected {err=}, {type(err)=}")

try:
    f = open('myfile.txt')
except OSError:
    print('Cannot open file')
else:
    print('File has', len(f.readlines()), 'lines')
    f.close()
