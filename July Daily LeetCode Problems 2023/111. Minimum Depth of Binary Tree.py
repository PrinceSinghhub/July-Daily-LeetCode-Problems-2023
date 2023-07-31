# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root):

        if root == None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0 or right == 0:
            return left + right + 1

        return min(left, right) + 1
