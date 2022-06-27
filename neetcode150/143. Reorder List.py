# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #n, 1
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #to get to the second half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next #+1
            fast = fast.next.next #+2
        
        rhead = slow.next #head of second half linked list
        
        prev, slow.next = None, None #slow.next = None coz ending first half
        #iterative reversal of second half
        while rhead:
            rnxt = rhead.next
            rhead.next = prev
            prev = rhead
            rhead = rnxt
        
        
        first, second = head, prev #head is head of first half, prev is head of second
        while second: #since second could be shorter than first half
            fnxt = first.next
            snxt = second.next
            #alternatively mixing the two lists
            first.next = second
            second.next = fnxt
            first, second = fnxt, snxt
            