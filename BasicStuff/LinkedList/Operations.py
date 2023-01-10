class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self):
        self.head = None

#  _________________________________________________
# _________________ Insert at the beginning ________\   

    def insert_at_start(self, data):
        # 1. create a node
        new_node = Node(data)
        # 2. set next pointer - the next pointer is previous head of ll
        new_node.next = self.head
        # 3. Set the new node as the head of the ll
        self.head = new_node
#  _________________________________________________
# _________________ Insert at middle   _____________\   

    def insert_at_middle(self,prev_node,data):
        # the previous node can not be None
        if prev_node:
            new_node = Node(data)
            new_node.next = prev_node.next
            prev_node.next = new_node
        else:
            print("previous node can not be none, that must exist in the linked list")
            return

#  _________________________________________________
# _________________ Insert at middle   _____________\   

    def insert_at_end(self,data):
        new_node = Node(data)
        # 1. If the linked list is empty then
        if self.head is None:
            self.head = new_node
            return
        # 2. if the ll is not empty then, we have to reach the end
        #   to reach the end we have to traverse until the head is None
        last = self.head # startinh here
        while last.next: 
            last = last.next
        # while loop ends when next of last is none, means it is the last value
        last.next = new_node

# _________________________________________________
# ___________________Traverse or print a ll________\

    def print_ll(self):
        temp = self.head
        while temp:
            print(temp.data , end=" ")
            temp = temp.next
        print("")

if __name__ == "__main__":
    # __________________________________________________________________________________
    ll = LinkedList()
    # create linked list first : create nodes + connect them
    # creating  nodes
    ll.head = Node(0)
    first = Node(1)
    second = Node(2)
    # connect nodes
    ll.head.next = first
    first.next = second

    ll.print_ll()
    ll.insert_at_start(4)
    ll.print_ll()
    # __________________________________________________________________________________

    # ____________________________ insert at start and check
    ll2 = LinkedList()
    ll2.insert_at_start(4)
    ll2.print_ll()
    ll2.insert_at_start(5)
    ll2.print_ll()
    ll2.insert_at_start(6)
    ll2.print_ll()
    # __________________________________ insert at middle and check
    ll2.insert_at_middle(ll2.head.next,7)
    ll2.print_ll()
    ll2.insert_at_middle(ll2.head.next,9)
    ll2.print_ll()
    # ____________________________ insert at end and check

    ll2.insert_at_end(11)
    ll2.print_ll()
    ll2.insert_at_end(12)
    ll2.print_ll()
    # __________________________________________________________________________________
