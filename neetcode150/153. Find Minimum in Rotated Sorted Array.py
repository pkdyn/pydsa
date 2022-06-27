class Solution:
    #logn, 1
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] 
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]: #if arr is sorted
                res = min(res, nums[l])
                break

            m = (l + r) // 2  #if not sorted
            res = min(res, nums[m])
            if nums[l] <= nums[m]: #currently in left portion
                l = m + 1 #search right portion
            else: #in right portion
                r = m - 1 #search left portion
        return res
            