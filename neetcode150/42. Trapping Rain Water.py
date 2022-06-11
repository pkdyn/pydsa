class Solution:
    #n, 1
    def trap(self, height: List[int]) -> int:
        
        if not height: #empty array
            return 0
        
        l, r = 0, len(height) - 1
        Lmax = height[l]
        Rmax = height[r]
        res = 0
        while l < r:
            #forml: min(Rmax, Lmax)(including current height) - height[i]
            if Lmax < Rmax:
                l += 1 #edge blocks cant trap
                Lmax = max(Lmax, height[l])
                res += Lmax - height[l]
            else:
                r -= 1 #edge blocks cant trap
                Rmax = max(Rmax, height[r])
                res += Rmax - height[r]
                
        return res