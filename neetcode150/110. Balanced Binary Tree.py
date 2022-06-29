# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #n, n
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, -1] #if empty tree return true and its len -> -1
            left, right = dfs(root.left), dfs(root.right)#recursive call for child nodes
            balanced = left[0] and right[0] and abs(left[1] - right[1])<=1 
            #boolean val to check balancy
            #left[0] right[0] for ensuring children are balanced too
            return [balanced, 1 + max(left[1], right[1])]
            #1 + max(left[1], right[1]) returns the height till that node
        
        return dfs(root)[0]#return balancy uptill that node (bottom-up)
        