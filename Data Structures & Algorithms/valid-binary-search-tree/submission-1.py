# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=[]

        def turn_to_list(root):
            nonlocal res

            if not root:
                return
            
            turn_to_list(root.left)
            res.append(root.val)
            turn_to_list(root.right)
        
        turn_to_list(root)

        for i in range(len(res)):
            if i>0 and res[i]<=res[i-1]:
                return False
        
        return True
        