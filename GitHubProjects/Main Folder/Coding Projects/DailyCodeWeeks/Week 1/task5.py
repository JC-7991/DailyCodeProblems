def cons(a, b):
    return (a, b)

def car(pair):
    return pair[0]

def cdr(pair):
    return pair[1]

lst = cons(1, cons(2, 3))

print(car(lst))
print(car(cdr(lst)))
print(cdr(cdr(lst)))