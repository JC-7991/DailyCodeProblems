# tuples are faster than lists but are immutable
x = (1, 2, 3)
print(x, type(x))

list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))