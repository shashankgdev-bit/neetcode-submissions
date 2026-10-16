# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def countNodes(node, n):
            nonlocal count

            if not node:
                return

            if node.val >= n:
                count += 1

            countNodes(node.left,max(n, node.val))
            countNodes(node.right,max(n, node.val))

        countNodes(root, float('-inf'))
        return count