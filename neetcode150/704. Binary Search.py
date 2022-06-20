class Solution:
    #logn , 1
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0,  len(nums) - 1
        
        while low <= high: 
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid #return index
        return -1 #element not found
                