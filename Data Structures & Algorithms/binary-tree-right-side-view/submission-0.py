# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        que = deque()

        if root == None:
            return []

        que.append(root)

        while que:
            k = len(que)
            temp = []
            for i in range(k):
                p = que.popleft()
                temp.append(p.val)

                if p.left != None:
                    que.append(p.left)
                if p.right != None:
                    que.append(p.right)

            res.append(temp)

        fin = []

        for pos in res:
            fin.append(pos[-1])

        return fin    

