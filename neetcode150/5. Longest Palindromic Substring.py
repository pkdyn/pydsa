class Solution:
    def longestPalindrome(self, s: str) -> str:
        #n***3 naive: len of string (n) * n**2 substrings (each character(n)'s n str comb)
        #n**2 expand around center: (each centre character(2n-1) * non-centre length (n-1)), 1
        res = ""
        resLen = 0
        
        for i in range(len(s)): #for every position in str rather than every char in str
            # get odd length pals
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # get even length pals
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
                
        return res