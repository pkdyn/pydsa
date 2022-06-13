class Solution:
    #n, n
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cSet = set() #to track unique chars
        res = 0
        for r in range(len(s)):
            while s[r] in cSet:
                #note it's l not r
                cSet.remove(s[l])
                l += 1 #shift the left pointer to slide window
            cSet.add(s[r])
            res = max(res, r - l + 1) #len of window: r - l + 1
        return res