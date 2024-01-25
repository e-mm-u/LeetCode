# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(root, freq):
            if not root:
                return 0

            freq[root.val] += 1

            # leaf node
            if not root.left and not root.right:
                odd_count = 0
                for v in freq:
                    if v % 2 == 1:
                        odd_count += 1
                freq[root.val] -= 1
                return 1 if odd_count <= 1 else 0

            left_count = dfs(root.left, freq)
            right_count = dfs(root.right, freq)

            freq[root.val] -= 1

            return left_count + right_count

        freq = [0] * 10  # Assuming values in the tree are digits (0-9)
        return dfs(root, freq)