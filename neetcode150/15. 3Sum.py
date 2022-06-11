class Solution:
    #nlogn,  n
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: #ensure no duplicates for fi
                continue
            fi = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = fi + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else: 
                    res.append([fi, nums[l], nums[r]])
                    l += 1
                    #ensuring no duplicates for second value
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res
