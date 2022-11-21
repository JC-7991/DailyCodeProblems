class Node:

    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def kthLast(node, k):

    count = 0
    var = node
    current = node

    while current:

        count += 1
        if count > k:
            var = var.next
        current = current.next

    return var.val