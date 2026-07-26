# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        
        left=self.diameterOfBinaryTree(root.left)
        right=self.diameterOfBinaryTree(root.right)

        cur=self.maxheight(root.left)+self.maxheight(root.right)

        return max(cur,left,right)
    
    def maxheight(self,root):
        if not root:
            return 0
        
        left=self.maxheight(root.left)
        right=self.maxheight(root.right)

        return max(left,right)+1
        