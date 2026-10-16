# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q.append(root)
        result = []
        if root is None:
            return []

        while q:
            k = len(q)
            memo = []
            for i in range(k):
                temp = q.popleft()

                memo.append(temp.val)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)

            result.append(memo)

        return result

