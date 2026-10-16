# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float('-inf')

        def path(node):
            nonlocal global_max
            if not node:
                return 0

            left_sum = max(path(node.left), 0)
            right_sum = max(path(node.right), 0)

            current = left_sum + right_sum + node.val
            global_max = max(global_max, current)

            return node.val + max(left_sum, right_sum)

        path(root)
        return global_max
        