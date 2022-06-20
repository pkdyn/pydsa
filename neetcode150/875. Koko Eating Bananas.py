class Solution:
    #nlog(m), 1
    #m is max(piles)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #left and right pointers over range(0, max(piles) + 1)
        k = 0
        
        while l <= r:
            m = (l + r) // 2
            hrs = 0 
            for p in piles:
                hrs += math.ceil(p / m) #calculating time to eat all piles for k = m
                #ceiling it to account for 1hr if p/m < 1
            if hrs <= h: #m is workable speed
                k = m     #m bananas/hr is the minimum speed yet
                r = m - 1 #shift right pointer to left of mid for a possible smaller m
            else: #m too slow. binary srch in right range
                l = m + 1 #shift left pointer to right of mid
        return k
        