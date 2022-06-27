class Solution:
    #n , 1
    #alt: detecting the node that starts a cycle in linked list
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0
        #do-while loop
        while True: # until they intersect again
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
            
        slow2 = 0
        while True: #until they intersect 
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: 
                return slow2 #essentialy the node that starts the cycle in linked list