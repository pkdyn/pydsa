# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #n, 1
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head #at same position
        
        #essentially a do while loop by py doesnt support that
        #alt: while with a return / break
        while fast and fast.next: # since shifting by 2
            slow = slow.next #shift by 1
            fast = fast.next.next #shift by 2
            if slow == fast: #meet each other second time: cycle exists
                return True
        
        return False