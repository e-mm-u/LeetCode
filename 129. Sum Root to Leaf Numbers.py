# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, preSum):
            if not root:
                return 0
            totalSum = preSum*10+root.val

            if not root.left and not root.right:
                return totalSum
            
            leftSum = dfs(root.left, totalSum)
            rightSum = dfs(root.right, totalSum)
            
            return leftSum+rightSum

        return dfs(root,0)