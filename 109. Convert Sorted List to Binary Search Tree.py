# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # 1. find the middle or root node using pointer
        slow = fast = head
        prev = None # pre to track the end of a subtree
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # ___slow points to the root of tree/subtree and 
        # ___prev points where the subtree ends
        # 2. disconnect left subtree from the root -> [head .. pre]..[root]..[rest nodes]
        prev.next = None

        # 3. create the root/parent tree node
        root = TreeNode(slow.val)

        # use recursion to generate the left and right BST
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
