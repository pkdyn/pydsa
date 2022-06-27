# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #n, 1
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode() 
        dummy.next = head #to get the node prev of the one to be deleted
        slow, fast = dummy, head
        for x in range(0, n): #shifting fast by n position
            fast = fast.next
        
        
        while fast: #shifting both until fast reaches the end
            slow = slow.next
            fast = fast.next
        #slow is prev to node to be deleted
        slow.next = slow.next.next 
        head = dummy.next #we dont want to add dummy to the list
        return head