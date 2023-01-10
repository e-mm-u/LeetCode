class Node :
    # creating a node
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None

if __name__ == "__main__":
    ll = LinkedList()

    # assign item values
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)

    # connect the nodes
    ll.head.next = second
    second.next = third

    while ll.head :
        print(ll.head.item, end="-->")
        ll.head = ll.head.next
    print('None\n')

    