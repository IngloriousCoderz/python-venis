# First argument is file or module name, second argument must be set

from sys import argv

print(f"Message from {argv[0]}:")
print(f"Hello {argv[1]}!")
