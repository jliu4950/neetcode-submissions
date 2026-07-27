# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dq=deque([root])
        res=[]

        while dq:
            size=len(dq)
            for i in range(size):
                cur=dq.popleft()
                if i == size-1:
                    res.append(cur.val)
                
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
        
        return res
        