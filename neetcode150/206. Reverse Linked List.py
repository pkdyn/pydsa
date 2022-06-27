# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
iterative: n, 1
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
'''

class Solution:
    #n, n
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        if not head:
            return None #remb: None instead of null

        temp = head
        if head.next:
            temp = self.reverseList(head.next)
            head.next.next = head #reversing 
        head.next = None #former head is now the last element
        return temp #return the new head
        