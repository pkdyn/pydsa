class Solution:
    #n, n
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums) #create set out of list
        
        longest = 0
        for n in nums: #iterate thru ;ist not set
            
            if n-1 not in nSet:
                sz = 0
                while n + sz in nSet: #clever way to account for first element
                    sz += 1
                longest = max (longest, sz)
            
        return longest
            