class Solution:
    #logn, 1
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted region
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: #target in right region
                    l = mid + 1
                else:
                    r = mid - 1 #target in current region, update pointer
            
            #right sorted region
            else:
                if target < nums[mid] or target > nums[r]: #target in left region
                    r = mid - 1
                else:
                    l = mid + 1 ##target in current region, update pointer
        return -1
        