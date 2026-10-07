# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self,p,q):
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        left = self.isSubtree(root.left,subRoot) 
        right = self.isSubtree(root.right,subRoot)

        if left or right :
            return True
        if root.val == subRoot.val:
            return self.isSameTree(root,subRoot)
        else:
            return False

        