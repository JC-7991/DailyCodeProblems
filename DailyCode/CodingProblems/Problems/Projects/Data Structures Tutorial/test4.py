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
x.insert(1, 1.5)
x.pop()
x.remove(1)
x.reverse()
print(x)

x = [5, 8, 3, 6, 1]
x.sort()
print(x)

x.sort(reverse = True)
print(x)