class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_to_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def add_after_node(self, prev_node, data):
        if prev_node is None:
            print("Previous node is not in the linked list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.length += 1

    def add_before_node(self, next_node, data):
        if next_node is None:
            print("Next node is not in the linked list")
            return
        if next_node == self.head:
            self.add_to_begin(data)
            return
        current = self.head
        while current.next is not None:
            if current.next == next_node:
                new_node = Node(data)
                new_node.next = next_node
                current.next = new_node
                self.length += 1
                return
            current = current.next
        print("Next node is not in the linked list")

    def add_at_index(self, index, data):
        if index < 0 or index > self.length:
            print("Invalid index")
            return
        if index == 0:
            self.add_to_begin(data)
            return
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index")
            return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next
        self.length -= 1

    def remove_from_begin(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.length -= 1

    def remove_from_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.length -= 1
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        self.length -= 1

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def get_length(self):
        return self.length

    def get_node_at_index(self, index):
        if index < 0 or index >= self.length:
            print("Invalid index")
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current


ll = LinkedList()
ll.add_to_begin(5)
ll.add_to_begin(7)
ll.add_at_index(2,5)
ll.print_list()
print(ll.get_length())
ll.add_at_index(3,7)
ll.print_list()

