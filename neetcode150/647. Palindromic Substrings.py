class Solution:
    #n**2, 1
    #expand around the centre approach
    def countSubstrings(self, s: str) -> int:
        res =  0
        
        for i in range(len(s)): #for every position in str rather than every char in str
            # to get odd length pals
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            
            # to get even length pals
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
                
        return res