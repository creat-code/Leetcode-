# Last updated: 11/5/2026, 9:24:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #method 1
        # recursive

        if root==None:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        