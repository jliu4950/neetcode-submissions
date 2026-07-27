# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        dq=deque()

        def dfs(root):
            nonlocal dq

            if not root:
                return 
            
            dfs(root.left)
            dq.append(root.val)
            dfs(root.right)
        
        dfs(root)

        res=root.val
        for i in range(k):
            res=dq.popleft()
        
        return res
        

        