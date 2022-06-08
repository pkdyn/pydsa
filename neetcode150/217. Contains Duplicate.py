class Solution:
    #n, n
    def containsDuplicate(self, nums: List[int]) -> bool:
        hSet = set() #hashSet
        
        for n in nums:
            if n in hSet:
                return True
            hSet.add(n)
            
        return False
        