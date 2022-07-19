class Solution:
    #n , 1
    #dp[i] = dp, dp[i + 1] = dp1, ..
    def numDecodings(self, s: str) -> int:
        dp, dp1, dp2 = 0, 1, 0
        n = len(s)
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] != '0':
                dp += dp1
            if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
        return dp1
                