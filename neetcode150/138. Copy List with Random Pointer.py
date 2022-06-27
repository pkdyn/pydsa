"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    #n , n
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copydir = {None : None} #edge case: none would map to none
        
        curr = head
        #1st pass to copy nodes into hashMap
        while curr:
            copy = Node(curr.val)
            copydir[curr] = copy
            curr = curr.next
        
        curr = head
        #2nd pass to copy pointers
        while curr:
            copy = copydir[curr]
            copy.next = copydir[curr.next]
            copy.random = copydir[curr.random]
            curr = curr.next
        
        return copydir[head] #return copy head