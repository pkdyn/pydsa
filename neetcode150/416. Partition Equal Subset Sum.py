class Solution:
    #O(n*sum(nums)), O(sum(nums))
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        
        for n in nums:
            dpcpy = set()
            for d in dp:
                if d + n == target:
                    return True
                dpcpy.add(d)
                dpcpy.add(d + n)
            dp = dpcpy
        return False
        