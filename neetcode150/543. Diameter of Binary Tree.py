# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #n, 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0] #a single element list to take care of global variable errors
        #alt would be to use self.res everytime instead
        
        def dfs(root): #return height
            if not root:
                return -1 #empty node -> -1; single node ->0
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right) 
            #+2 due to edges (parent -> child)
            
            return 1 + max(left, right) #+1 due to edge connecting the child nodes
        
        dfs(root)
        return res[0]