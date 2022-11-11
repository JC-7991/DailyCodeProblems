# tuples are faster than lists but are immutable
# they're often used for fixed data
x = (1, 2, 3)
print(x, type(x))

z = (2, 5.5, 999)
print(z)

list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))

y = ([1, 2], 3)
del(y[0][1])
print(y)

y += (4, )
print(y)