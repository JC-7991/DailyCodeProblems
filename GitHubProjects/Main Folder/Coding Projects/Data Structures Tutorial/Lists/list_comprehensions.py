import random

# get values within a range
under_10 = [x for x in range(10)]
print('under_10: ' + str(under_10))

# get squared values within a range
squares = [x ** 2 for x in under_10]
print('squares: ' + str(squares))

# get odd values
odds = [x for x in range(10) if x % 2 == 1]
print('odds: ' + str(odds))