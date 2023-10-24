'single quotes are \'cool\''
'single quotes are "cool"'
"double quotes are \"cool\""
"double quotes are 'cool'"

'Some\name' # Watch out for backslashes, escape them
r'Some\name' # Or prepend 'r' for raw strings
who = 'ma'
f"Hello {who * 2}!" # 'f' interpolates Python expressions
b'Octect string' # sequence of bytes, convert to string with str.decode()

'''
String
Literals
'''
"""Span
multiple lines"""
"""\
Add the escape to
remove newlines\
"""

'Conca' + 'tenation'
16 * 'Na' + ' Batman!'
'Bat' 'man' # automatic concatenation
# 'Bat' who # doesn't work with variables

word = 'Python'
word[1] # second character
word[-1] # last character
word[2:5] # range
word[:2]
word[2:]
word[-2:]
word[:] # makes a copy of the string
word[42] # string index out of range
word[4:42] # slicing handles indexes gracefully
word[42:]

word[1] = 'e' # strings are immutable
word[0] + 'e' + word[2:]
len(word) # built-in function
