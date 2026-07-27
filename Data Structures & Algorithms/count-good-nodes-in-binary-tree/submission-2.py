class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root,path_max):
            if not root:
                return 0
            
            count=0
            if root.val>=path_max:
                count+=1
            
            new_max=max(path_max,root.val)
            count+=dfs(root.left,new_max)
            count+=dfs(root.right,new_max)

            return count
        
        return dfs(root,root.val)