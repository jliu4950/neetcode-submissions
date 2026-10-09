# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        res.append(True)
        
        def dfs(root,pre):
            if not root:
                return pre
            
            pre = dfs(root.left,pre) 
            if root.val <= pre:
                res[0] = False
            return dfs(root.right,root.val)
        
        dfs(root,float("-inf"))
        return res[0]