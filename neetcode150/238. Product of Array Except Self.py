class Solution:
    #n, n
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums) #array of n 1s
        pre = 1 #prefix multiplier
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
            
        post  = 1 #postfix multiplier
        for i in range(len(nums) - 1, -1 , -1): #reverse traverse whole array
            res[i] *= post 
            post *= nums[i]
        
        return res
        