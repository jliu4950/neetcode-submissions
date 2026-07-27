# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # base case
        if not preorder:
            return None

        root_val=preorder[0]
        root=TreeNode(root_val)

        #find index and lenth of subtree
        in_idx = inorder.index(root_val)
        leftlength = in_idx
        rightlength = len(inorder) - in_idx - 1

        # #lefttree
        # left_pre_start= 1
        # left_pre_end= leftlength+1
        # left_in_start= 0
        # left_in_end= leftlength
        # #righttree
        # right_pre_start= leftlength+1
        # right_pre_end= len(preorder)
        # right_in_start= in_idx+1
        # right_in_end= len(inorder)  

        root.left=self.buildTree(preorder[1:leftlength+1],inorder[0 : leftlength])
        root.right=self.buildTree(preorder[leftlength+1:len(preorder)],inorder[in_idx+1:len(inorder)])

        return root
        