class Solution:
    #n, n
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sdct, tdct = {}, {} #hashMaps: empty dict
        
        for i in range(len(s)):
            sdct[s[i]] = 1 + sdct.get(s[i], 0) #return zero if invalid key
            tdct[t[i]] = 1 + tdct.get(t[i], 0)
        
        for ch in sdct:
            if sdct[ch] != tdct.get(ch, 0): #ensure ch is a key in other dict too
                return False
        
        return True
            
        