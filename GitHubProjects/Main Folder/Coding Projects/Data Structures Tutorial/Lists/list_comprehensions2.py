s = "I love 2 go 2 the store 5 times a week."
nums = [x for x in s if x.isnumeric()]
print('nums: ' + ''.join(nums))

names = ['Sonic', 'Tails', 'Knuckles', 'Shadow']
idx = [k for k, v in enumerate(names) if v == 'Sonic']
print('index = ' + str(idx[0]))