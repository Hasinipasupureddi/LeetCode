# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # If the left subtree is empty, we must find the min depth of the right subtree
        if not root.left:
            return 1 + self.minDepth(root.right)
        # If the right subtree is empty, we must find the min depth of the left subtree
        if not root.right:
            return 1 + self.minDepth(root.left)
        # If both subtrees exist, take the minimum of both paths
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))