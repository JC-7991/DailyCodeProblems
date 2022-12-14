x = 'bug'
print(min(x))
print(max(x))

x = ['123', 'abc', 'you and me']
print(min(x))
print(max(x))

x = [1, 4, 7, 12]
print(sum(x))
print(sum(x[-2:]))

x = ['b', 'a', 'c', 'e', 'd']
print(sorted(x))

# sort by 2nd letter
x = ['Adam', 'Beck', 'Chad', 'Dairon']
print(sorted(x, key = lambda k: k[1]))

# sort by 3rd letter
print(sorted(x, key = lambda k: k[2]))

x = ['xxxcx', 'xxxax', 'xxxbx']
print(sorted(x, key = lambda k: k[3]))

x = 'hinglemccringleberry'
print(x.count('e'))
print(x.index('r'))

a = [m for m in range(8)]
print(a)

b = [i ** 2 for i in range(10) if i > 4]
print(b)

c = [i ** 3 for i in range(15) if i > 3]
print(c)