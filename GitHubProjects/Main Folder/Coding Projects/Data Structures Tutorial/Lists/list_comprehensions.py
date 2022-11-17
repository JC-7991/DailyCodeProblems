import random

# get values within a range
under_10 = [x for x in range(10)]
print('under 10s: ' + str(under_10))

# get squared values within a range
squares = [x ** 2 for x in under_10]
print('squares: ' + str(squares))

# get odd values
odds = [x for x in range(10) if x % 2 == 1]
print('odds: ' + str(odds))

# get even values
evens = [x for x in range(10) if x % 2 == 0]
print('evens: ' + str(evens))

# get multiples of five
fives = [x for x in range(50) if x % 5 == 0]
print('fives: ' + str(fives))