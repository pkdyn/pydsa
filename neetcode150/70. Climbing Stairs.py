class Solution:
    #n(h/t: memoization/caching), 1 (instead of having a dp array, just keep two variables)
    #memoization reduces complexity fromm 2**n to n by linearizing the decision tree via caching
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(n-1):
            two, one = one, two + one
        return one
        
        