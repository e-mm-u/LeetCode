# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ________________________
# __ Recursive DFS ________\
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        cnt1 = 1 + self.maxDepth(root.left)
        cnt2 = 1 + self.maxDepth(root.right)
        return max(cnt1,cnt2)
    
# ________________________
# __ using queue  ________\
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        length = 0
        while q:
            for i in range(len(q)):
                popped = q.popleft()
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
            length += 1
        
        return length

# ________________________
# __ BFS -> using stack  ________\
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [root,1]

        [node,length] = stack.pop()

            
            
