class Solution:
    #n, 1
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        
        res = 0
        while l < r:
            area = (r - l) * min (height[l], height[r])
            res = max (res, area)
            
            #update the smaller height poointer
            if height[l] < height[r]: 
                l += 1
                
            else :
                r -= 1
        
        return res