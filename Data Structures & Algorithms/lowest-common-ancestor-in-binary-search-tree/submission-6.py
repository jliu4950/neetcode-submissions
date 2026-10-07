# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        1. 如果root 为p or q,return root
        2. 递归左右
        3. 左右非空,返回root
        4. 左右有一个非空，返回一边
        5. 左右都空,返回None
        '''

        if not root:
            return False
        
        if root is p or root is q:
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        elif left or right:
            return left if left else right
        else:
            return None