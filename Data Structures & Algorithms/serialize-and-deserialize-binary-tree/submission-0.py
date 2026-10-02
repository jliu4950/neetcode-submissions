# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        tree_str = []
        def dfs(root):
            if not root:
                tree_str.append("#")
                return
            
            tree_str.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return " ".join(tree_str)      
    # 1,2,#,#,3,4,#,#,5,#,#
    def deserialize(self, data):
        tree_list = data.split(" ")
        self.pos = 0
        def dfs():
            if tree_list[self.pos] == "#":
                self.pos += 1
                return None
            
            node = TreeNode(int(tree_list[self.pos]))
            self.pos += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()  
