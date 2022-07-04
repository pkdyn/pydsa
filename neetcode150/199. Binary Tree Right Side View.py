# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #logn, n
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            lvl = []
            for i in range(len(q)):
                tnode = q.popleft()
                if tnode:
                    lvl.append(tnode.val)
                    q.append(tnode.left)
                    q.append(tnode.right)
            if lvl:
                res.append(lvl[-1])
        return res
            