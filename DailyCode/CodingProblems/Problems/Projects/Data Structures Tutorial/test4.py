x = [5, 7, 9, 11]
del(x[1])
print(x)

x.append(7)
print(x)

del(x[3])
print(x)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
x.extend(y)
print(x)