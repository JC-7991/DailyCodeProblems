y = {'pork': 25.3, 'beef': 33.8, 'fish': 50}

print(y.keys())
print(y.values())
print(y.items())

print('beef' in y)
print('clams' in y.values())
print(25.3 in y.values())

# these values will not be printed in any sorted order
for key in y:
    print(key, y[key])

for k, v in y.items():
    print(k, v)