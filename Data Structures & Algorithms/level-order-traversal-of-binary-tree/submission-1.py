# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)

        def dfs(root,level):
            if not root:
                return
            
            dic[level].append(root.val)
            dfs(root.left,level + 1)
            dfs(root.right,level + 1)

        dfs(root,0)
        
        res = [ val for val in dic.values()]

        return res