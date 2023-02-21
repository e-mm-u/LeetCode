class Node : 
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, " > ")
            temp = temp.next
        print("end")

    def get_length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def insert_at_end(self,data):
        node = Node(data,None)
        if self.head is None:
            self.head = node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            # node = Node(data,self.head)
            # self.head = node
            self.insert_at_start(data)
            return
        
        count = 0
        temp = self.head

        while temp :
            if count==index-1:
                node = Node(data,temp.next)
                temp.next = node
                break
            temp = temp.next
            count += 1
    
    def remove_at(self,index):

        if index<0 or index>self.get_length():
            raise Exception
        
        if index==0:
            self.head = self.head.next
            return

        count = 0
        temp = self.head
        while temp:
            if count == index-1:
                temp.next = temp.next.next
                break
            temp = temp.next
            count += 1
    

        
            





if __name__ == '__main__':
    ll = LinkedList();
    ll.insert_at_start("hello")
    ll.insert_at_start("world")
    ll.insert_at(2,'blabla')
    ll.print()