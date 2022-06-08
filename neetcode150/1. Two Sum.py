class Solution:
    #n, n
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idxMap = {}
        
        for i, n in enumerate(nums): #unpacking into two var
            diff = target - n
            if diff in idxMap:
                return [idxMap[diff], i]
            idxMap[n] = i
            
        return
        