class Solution:
    #n*2^n, n*n
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, subset = [], []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) 
                #copy bcause same list is gonna be used for other cases
                return
            
            subset.append(nums[i])
            dfs(i + 1)
            
            subset.pop()
            dfs(i + 1)     
            
        dfs(0)
        return res