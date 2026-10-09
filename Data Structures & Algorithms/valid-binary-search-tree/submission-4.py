# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        pre = float("-inf")
        def dfs(root):
            nonlocal res
            nonlocal pre

            if not root:
                return
            dfs(root.left)
            if root.val <= pre:
                res = False
            pre = root.val
            dfs(root.right)
        
        dfs(root)
        return res
            