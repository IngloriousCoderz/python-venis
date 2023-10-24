message = 'hello world!'
message.upper() # 'HELLO WORLD!'
message.title() # 'Hello World!'
message.center(20) # '    hello world!    '
'Remove newline \n'.rstrip() # Removes any trailing space and newline
b'Octet string'.decode() # convert to string

message.split(' ') # ['Hello', 'world!']
'/'.join(('home', 'iceonfire', 'projects')) # home/iceonfire/projects

# Remember: strings are immutable!

# For extra features of string @see https://www.w3schools.com/python/python_ref_string.asp

'00:AC:B2'.split(':')
':'.join(['00', 'AC', 'B2'])
