class Solution(object):
    #n, 1
    def rob(self, nums):
        #call linRob on subarrays excluding first and last elements respectively
        def linRob(nums): #house robber 1 helper func
            rob1, rob2 = 0, 0
            for n in nums:
                rob1, rob2 = rob2, max(rob1 + n, rob2)
            return rob2
        
        if len(nums) == 1:
            return nums[0]
        else:
            return max(linRob(nums[1:]), linRob(nums[:-1]))
        