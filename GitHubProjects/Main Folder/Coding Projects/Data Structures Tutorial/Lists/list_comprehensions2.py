import random

s = "I love 2 go 2 the store 5 times a week."
nums = [x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums))

names = ['Sonic', 'Tails', 'Knuckles', 'Shadow']
idx = [k for k, v in enumerate(names) if v == 'Sonic']
print('index = ' + str(idx[0]))

idx = [k for k, v in enumerate(names) if v == 'Shadow']
print('index = ' + str(idx[0]))

idx = [k for k, v in enumerate(names) if v == 'Tails']
print('index = ' + str(idx[0]))

letters = [x for x in 'ABCDEFG']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']
print(letters, letrs)