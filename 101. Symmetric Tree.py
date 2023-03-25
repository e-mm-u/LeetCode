# ------------------- d f s ---------------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return False
        
        def isMirror(node1,node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            if node1.val!=node2.val:
                return False
            
            return isMirror(node1.left, node2.right) and isMirror(node1.right,node2.left)
        return isMirror(root.left,root.right)
        
# ---------------- b f s --------
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return False
        
        q = [root.left, root.right]
        while len(q)>0:
            node1 = q.pop(0)
            node2 = q.pop(0)

            if not node1 and not node2:
                continue

            if not node1 or not node2:
                return False

            if node1.val != node2.val:
                return False 


            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right) 
            q.append(node2.left)
            
        return True
                   