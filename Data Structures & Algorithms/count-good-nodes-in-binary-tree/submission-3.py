# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,max_val):
            #base case
            if not root:
                return 0

            left = dfs(root.left,max(root.val,max_val))
            right = dfs(root.right,max(root.val,max_val))
            
            return left + right + 1 if root.val >= max_val else left + right

        return dfs(root,float("-inf"))
        