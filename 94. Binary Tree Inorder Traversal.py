# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        curr = root
        while curr or stack:
            # while curr node is not null, traverse the left wing
            while curr:
                stack.append(curr)
                curr = curr.left

            # while loops end when there is no more left node
            # as it is inorder traversal, and there is no left, so append the node to res
            # and then move to the right wing
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        
        return ans

            

