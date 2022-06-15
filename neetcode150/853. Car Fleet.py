class Solution:
    #nlogn, n
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #combine and sort given arrays followed by list comprehension for time formula
        time = [(target - p)/s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in time[::-1]: #iterate through reverse list
            if t > cur:
                cur = t
                res += 1
        
        return res