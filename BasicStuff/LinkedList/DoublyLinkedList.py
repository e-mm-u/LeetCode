class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class Doubly_Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        if temp:
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            print("The list is empty")
    
    def get_length(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count

    def insert_at_start(self,data):
        node = Node(data)
        # check if the ll i empty
        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def insert_at_end(self,data):
        node = Node(data)
        # if empty:
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            
            node.prev = temp
            temp.next = node

    def insert_at_index(self,data,index):
        node = Node(data)
        temp = self.head
        length = self.get_length()

        if index<0 or index>length:
            print("Index out of range")
            return

        if index==0:
            self.insert_at_start(data)
            return
        
        count = 0
        while temp:
            if count == index-1:
                node.prev = temp
                node.next = temp.next
                temp.next.prev = node
                temp.next = node
            temp = temp.next
            count += 1

    def delete_at_index(self,index):
        count = 0
        temp = self.head

        while temp:
            if count == index-1:
                temp.next.prev = temp
                temp.next = temp.next.next
            
            temp = temp.next
            count += 1

    # insert after reference node
    # insert before reference node
    # insert at index
    # delete reference node
    # delete at index
    # get node a at index
    # get lenght of the ll
    # 
    # def insert_at_start(self,data):
    #     node = Node(data)
    #     node.next = self.head
        
    #     if self.head:
    #         self.head.prev = node

    #     self.head = node

dll = Doubly_Linkedlist()
node1 = Node(3)
dll.print_list()

dll.insert_at_start("hihi")
dll.insert_at_start(4)
dll.insert_at_start("haha")
dll.insert_at_end("0")
dll.insert_at_end("hoho")
dll.insert_at_index(1,0)
dll.insert_at_index('four',4)
dll.insert_at_index('six',6)

dll.print_list()
print("Length : ", dll.get_length())

dll.delete_at_index(4)
print("Length : ", dll.get_length())
dll.print_list()

dll.delete_at_index(2)
print("Length : ", dll.get_length())
dll.print_list()

dll.delete_at_index(3)
print("Length : ", dll.get_length())
dll.print_list()

dll.delete_at_index(0)
print("Length : ", dll.get_length())
dll.print_list()
