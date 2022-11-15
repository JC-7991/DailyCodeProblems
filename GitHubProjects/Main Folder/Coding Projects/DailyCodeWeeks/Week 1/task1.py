pairs = [10, 15, 3, 7, 15, 2]
k = 17
counter = 0

for i in pairs:
    if k - i in pairs:
        counter += 1

print(counter // 2)