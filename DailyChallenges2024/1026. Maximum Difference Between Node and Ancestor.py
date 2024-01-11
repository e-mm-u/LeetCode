# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node,minn,maxx):
            if not node:
                return (maxx-minn)
            
            maxx = max(maxx, node.val)
            minn = min(minn, node.val)

            leftDiff = dfs(node.left, minn, maxx)
            rightDiff = dfs(node.right, minn, maxx)

            return max(leftDiff, rightDiff)
        
        return dfs(root, root.val, root.val)
        