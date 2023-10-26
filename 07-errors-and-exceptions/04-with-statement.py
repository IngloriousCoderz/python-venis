f = None
try:
    f = open('myfile.txt')
    print(f.read())
except FileNotFoundError:
    print('File not found')
finally:
    if f is not None:
        print('Closing file...', end=' ')
        f.close()
        print('Done.')

with open('myfile.txt') as f:
    print(f.read())
