class Solution:
    #n, 1
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            sum = numbers[r] + numbers[l]
            if  sum > target:
                r -= 1
            elif  sum < target:
                l += 1
            else:
                return [l + 1, r + 1] #Q wants index starting from 1
        
        return