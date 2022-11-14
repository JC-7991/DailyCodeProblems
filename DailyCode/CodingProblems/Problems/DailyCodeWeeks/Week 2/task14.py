import random
 
INT = 1000
circle = 0
square = 0
 
for i in range(INT ** 2):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    origin_dist = x ** 2 + y ** 2

    if origin_dist <= 1:
        circle += 1
 
    square += 1
    pi = 4 * circle / square
 
print("Pi =", pi)