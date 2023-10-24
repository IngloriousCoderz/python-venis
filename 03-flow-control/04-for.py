print('Items:')
items = ['apple', 'orange', 'banana']
for item in items:
  print(item)

print('Simple range:')
for i in range(6):
  print(i)

# range is not a list, even though it's iterable: it's a sequence (like lists and tuples)
print(range(3)) # prints range(3)
print(list(range(3))) # prints [0, 1, 2]

print('Even numbers:')
for even in range(2, 12, 2): # optional start and step
  print(even)

print('Sum of first 4 numbers:')
print(sum(range(1, 5))) # built-in function

for i in range(len(items)):# similar to the classic 'for' loop
  print(i, items[i])

# break and else
for num in range(1, 6):
  if num % 2 == 0:
    print("Found an even number:", num)
    break
else: # Python-only, @see https://www.pythontutorial.net/python-basics/python-while-else/
  print('No even numbers found')

# continue
for num in range(1, 6):
  if num % 2 == 0:
    print("Found an even number:", num)
    continue
  print("Found an odd number:", num)

# pass is a placeholder for doing nothing
while True:
  pass
