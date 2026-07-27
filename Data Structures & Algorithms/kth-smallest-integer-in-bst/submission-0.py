# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        hp=[]

        def dfs(root):
            nonlocal hp

            if not root:
                return 
            
            dfs(root.left)
            heapq.heappush(hp,root.val)
            dfs(root.right)
        
        dfs(root)

        res=root.val
        for i in range(k):
            res=heapq.heappop(hp)
        
        return res
        

        