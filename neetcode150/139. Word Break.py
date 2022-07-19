class Solution:
    #s**2 * w, s
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        d = [False] * len(s)
        
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i + 1 - len(w):i + 1] and (d[i - len(w)] or i - len(w) == -1):
                    d[i]  = True
        return d[-1]