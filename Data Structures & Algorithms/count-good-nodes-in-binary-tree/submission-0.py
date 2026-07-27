# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path=[] # 
        res=[]
        
        def build(root):
            nonlocal path
            nonlocal res

            if not root:
                return
            
            if not path:
                res.append(root.val)
            else:
                path.sort()
                if root.val>=path[-1]:
                    res.append(root.val)
            
            path.append(root.val)
            build(root.left)
            build(root.right)
            path.remove(root.val) #无法确定排序后的删除是否有问题
        
        build(root)
        return len(res)