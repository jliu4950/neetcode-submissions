# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0

        def build(root,path_max):
            nonlocal res
            
            if not root:
                return
            
            if root.val>=path_max:
                res+=1
            build(root.left,max(path_max,root.val))
            build(root.right,max(path_max,root.val))
        
        build(root,-101)
        return res
            
