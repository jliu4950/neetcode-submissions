# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root,lower,upper):
            if not root:
                return True
            
            left = valid(root.left,lower,root.val)
            right = valid(root.right,root.val,upper)

            if not (left and right):
                return False
            
            if root.val<upper and root.val>lower:
                return True
        
        return valid(root,float("-inf"),float("inf"))
        