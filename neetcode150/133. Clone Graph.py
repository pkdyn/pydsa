"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    #v + e, v
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloneDir = {}
        
        def dfs(node):
            if node in cloneDir:
                return cloneDir[node]
            
            clone = Node(node.val)
            cloneDir[node] = clone
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        
        return dfs(node) if node else None
            