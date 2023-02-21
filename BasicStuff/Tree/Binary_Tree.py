class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
    
    def preorder(self):
        print(self.val, end=' ')

        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    
    def inorder(self):

        if self.left:
            self.left.inorder()
        print(self.val, end=' ')
        if self.right:
            self.right.inorder()
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val, end=' ')

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

#     # Traverse preorder
#     def preorder(self):
#         print(self.val, end=' ')
#         if self.left:
#             self.left.preorder()
#         if self.right:
#             self.right.preorder()

#     # Traverse inorder
#     def inorder(self):
#         if self.left:
#             self.left.inorder()
#         print(self.val, end=' ')
#         if self.right:
#             self.right.inorder()

#     # Traverse postorder
#     def postorder(self):
#         if self.left:
#             self.left.postorder()
#         if self.right:
#             self.right.postorder()
#         print(self.val, end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

print("traversing pre order\n")
root.preorder()
print("traversing in order\n")
root.inorder()
print("traversing post order\n")
root.postorder()

