# stacks are LIFO (Last In, First Out)
# all push/pop operations are to/from the top of the stack
# peek - get item from the top of the stack without removing it

# stack implementation using list
my_stack = list()

my_stack.append(4)
my_stack.append(10)
my_stack.append(3)

print(my_stack)
print(my_stack.pop())
print(my_stack)