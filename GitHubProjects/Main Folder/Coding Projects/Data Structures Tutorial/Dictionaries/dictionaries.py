# dictionaries have key-value pairs
# dictionaries are unordered, thus elements cannot be ordered

x = {'pork': 25.5, "beef": 34.5, "fish": 30}
print(x)

x = dict(pork = 25.5, beef = 34.5, fish = 30)
print(x)

x['pork'] = 100
del(x['beef'])
print(len(x))
print(x)

x.clear()
print(x)