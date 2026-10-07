# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        1. left have and right have :return root
        2. one side have and root.val == p/q: return root
        3. one side have and root.val != p/q: return that side
        4. both left and right don't have and root.val ! = p/q : return None
        5. both left and right don't have and root.val = p/q : return root
        
        '''
        if not root:
            return None
        print(root.val)
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        elif (left or right):
            if (root == q or root == p):
                return root
            else:
                return left if left else right
        elif root == p or root == q:
            return root
        else:
            return None