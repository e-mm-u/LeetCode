# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def inorder(root,q):
            if root:
                inorder(root.left,q)
                inorder(root.right,q)
                q.append(root.val)
            else:
                q.append(None)
            
            return q

        q1 = inorder(p,[])
        q2 = inorder(q,[])
        print(q1)
        print(q2)

        return q1==q2
        