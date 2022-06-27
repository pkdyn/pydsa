# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #n , 1
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() #to take care of edge case of inserting into empty list
        tail = dummy
        
        while l1 and l2: #while both have the same length, insert the smaller val
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next #dont forget to iterate the tail and respective list
        
        #if either exists after the other has ran out, append it to tail
        if l1: 
            tail.next = l1
        elif l2:
            tail.next = l2
        
        return dummy.next #since tail is at the end
        