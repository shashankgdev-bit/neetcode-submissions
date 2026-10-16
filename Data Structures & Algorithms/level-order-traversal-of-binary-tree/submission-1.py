# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traverse(root: Optional[TreeNode],level,temp):
            nonlocal result

            if root is None:
                return

            if level == len(result):
                result.append([])

            result[level].append(root.val)

            traverse(root.left,level+1,temp)
            traverse(root.right,level+1,temp)

            return
        
        traverse(root,0,[])

        return result


