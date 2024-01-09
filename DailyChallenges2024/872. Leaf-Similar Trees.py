# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def traverse(root,arr):
            if(not root.left and not root.right):
                arr.append(root.val)
            
            if(root.left):
                traverse(root.left, arr)
            if(root.right):
                traverse(root.right, arr)
            
            return arr
        return traverse(root1, [])==traverse(root2, [])