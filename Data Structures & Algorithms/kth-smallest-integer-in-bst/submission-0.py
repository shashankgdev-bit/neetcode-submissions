# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = -1

        def bst(node, k):
            nonlocal count
            nonlocal result

            if not node:
                return

            bst(node.left, k)
            count += 1

            if(count == k):
                result = node.val
                return 

            bst(node.right, k)

            return

        bst(root,k)
        return result
            