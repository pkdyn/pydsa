# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #n, n
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stck = [root]
        while stck:
            node = stck.pop()
            if node:
                node.left, node.right = node.right, node.left
                stck.append(node.left)
                stck.append(node.right)
        return root
                
        
        
'''
if not root:
    return None
root.left, root.right = root.right, root.left #swap root's chilren

self.invertTree(root.left) #do the same for left child
self.invertTree(root.right)# do the same for right child
return root
'''
        
    