# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        hp=deque()
        res=[]
        hp.append(root)

        while hp:
            size=len(hp)
            sublist=[]
            for _ in range(size):
                cur=hp.popleft()
                if cur.left:
                    hp.append(cur.left)
                if cur.right:
                    hp.append(cur.right)
                sublist.append(cur.val)
            
            res.append(sublist)
        
        return res

        