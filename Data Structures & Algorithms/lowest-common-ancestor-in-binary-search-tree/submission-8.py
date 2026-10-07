# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        利用BST特性
        * 如果 p、q 都在左边 → 去左子树，此时 p、q 一定都在左子树里
        * 如果 p、q 都在右边 → 去右子树，此时 p、q 一定都在右子树里
        * 否则 → 当前位置就是答案，直接返回
        '''
        if not root:
            return None
        
        if max(p.val,q.val) < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        elif min(p.val,q.val) > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
