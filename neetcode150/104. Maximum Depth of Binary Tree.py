# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
        
class Solution:
    #n, n
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stck = [[root, 1]] #list of list of pairs
        res = 0

        while stck:
            node, depth = stck.pop()
            if node:
                res = max(res, depth)
                stck.append([node.left, depth + 1])
                stck.append([node.right, depth + 1])
        return res
            
'''
recursive
#n, n
def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root: #no node -> 0 depth
        return 0 
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #note it's 1 + max(left, right)
'''
    