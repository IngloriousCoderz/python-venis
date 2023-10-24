basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print(basket) # prints {'banana', 'pear', 'orange', 'apple'}, in a seemingly random order

fruit = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(fruit)
print('orange' in fruit) # returns True
print('mango' in fruit) # returns False

a = set('abracadabra')
a # prints {'c', 'd', 'b', 'r', 'a'}
b = set('alacazam')
a - b # difference
a & b # intersection
a | b # union
a ^ b # symmetric difference: union minus intersection

print(list(set(basket))) # doesn't preserve items order!
