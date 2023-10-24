# Usage:
# python 01-first-script.py
# or
# python -m 01-first-script

2 + 2 # seems to do nothing
print(2 + 2) # prints '4'

# Sidenote: let's play with the print function

print('Hello', 'world') # multiple args are concatenated

print('Hello', 'world', sep=', ') # custom separator
print('home', 'iceonfire', 'code', sep='/') # useful for paths

print('Hello', 'world', end='!\n') # custom end
print('Checking file integrity...', end='') # prevent line breaks
print('ok')
