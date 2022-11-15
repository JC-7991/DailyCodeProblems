class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
 
def getIntersectionNode(head1, head2):

    while head2:

        temp = head1

        while temp:

            if temp == head2:
                return head2
            temp = temp.next

        head2 = head2.next

    return None

if __name__ == '__main__':

    newNode = Node(10)
    head1 = newNode

    newNode = Node(3)
    head2 = newNode

    newNode = Node(6)
    head2.next = newNode

    newNode = Node(9)
    head2.next.next = newNode

    newNode = Node(15)
    head1.next = newNode

    head2.next.next.next = newNode
    newNode = Node(30)
    
    head1.next.next = newNode
 
    intersectionPoint = getIntersectionNode(head1, head2)
 
    if not intersectionPoint:
        print("No Intersection Point.")

    else:
        print("Intersection Point:", intersectionPoint.data)