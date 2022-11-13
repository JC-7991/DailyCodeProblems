# sets store non-duplicate values
# faster access compared to lists

x = {3, 5, 3, 5, 9}
print(x)

y = set()
print(y)

list1 = [1, 2, 4, 4]
z = set(list1)
print(z)

x = {3, 5, 7, 9}
x.add(7)
x.remove(3)
print(len(x))
print(x.pop(), x)
x.clear()
print(x)