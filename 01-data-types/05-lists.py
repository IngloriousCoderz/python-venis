squares = [1, 4, 9, 16, 25]
squares[2:4] # slicing applies exactly as in strings
squares[:] # shallow copy
squares + [36, 49, 64] # concatenation

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64 # lists are mutable
cubes.append(6 ** 3)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
letters[2:5] = []
letters[:] = [] # empty the list
len(letters) # built-in function

matrix = [squares, cubes, letters] # nested lists
matrix[1]
matrix[1][3]

potpourri = [1, 'two', [3]] # you can mix any types