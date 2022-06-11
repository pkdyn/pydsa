class Solution:
    #n, n
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums) #create set out of given list
        
        longest = 0
        for n in nums: #iterate thru list not set. n is element not index
            if n-1 not in nSet: #no previous consecutive value
                sz = 0
                while n + sz in nSet: #clever way to account for first element
                    sz += 1
                longest = max (longest, sz)
            
        return longest
            