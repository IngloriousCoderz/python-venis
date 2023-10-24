my_list = [1, 2, 3]

my_list.append(4)
my_list = my_list + [5] # equivalent to above
my_list[len(my_list):] = [6] # equivalent to above

my_list.extend([6, 7])
my_list.extend(range(8, 10)) # equivalent to above
my_list[len(my_list):] = [8, 9, 10] # equivalent to above

my_list.insert(index, item)
my_list.remove(item) # removes first occurence, raises error if no such item
my_list.pop(index) # removes item and returns it
my_list.pop() # removes last item and returns it

my_list.clear()
del my_list[:] # equivalent to above
# digression: the del statement removes iems by index(es)
del my_list[0]
del my_list[2:4]
del my_list[:]
del my_list # removes the variable
del _ # doesn't work!

my_list.index(item) # returns index of first occurrence
my_list.index(item, start, end) # optional args limit the search

my_list.count(item) # counts occurrences
my_list.sort() # sorts items alphabetically and numerically, for optional args @see https://docs.python.org/3/library/functions.html#sorted
my_list.reverse() # reverses the list
my_list.copy() # creates a shallow clone
my_list[:] # equivalent to above
