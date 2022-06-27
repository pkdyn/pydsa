# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #n ,1
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getKth(groupPrev, k) #func to get kth node wrt to arg node
            if not kth: #ungrouped element (last for example)
                break #gets us out of infinite true
            groupNext = kth.next
            
            # reverse group
            prev, curr = kth.next, groupPrev.next 
            #kth.next to not break linked list while reversing
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            #update nodes connected to rev grp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp #setting grprev for next group
        return dummy.next 
    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
        