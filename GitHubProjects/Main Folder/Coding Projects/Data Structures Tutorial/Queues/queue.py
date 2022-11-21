# queue's are First-In, First-Out
# enqueue - add item to the end of the line
# dequeue - remove item from the front of the line

from collections import deque

my_queue = deque()
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())
print(my_queue)