class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def bcktrck(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
        
            subset.append(nums[i])
            bcktrck(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums)  and nums[i] == nums[i + 1]:
                i += 1
            bcktrck(i + 1, subset)
        bcktrck(0, [])
        return res