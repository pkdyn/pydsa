class Solution:
    #n, 1
    def isPalindrome(self, s: str) -> bool:
        '''
        newStr = ""
        
        for ch in s:
            if ch.isalnum(): #not isalnum(ch)
                newStr += ch.lower()
        
        return newStr == newStr[::-1] #compare string with its reverse
        '''
        
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not self.alnum(s[l]): #self cauze calling func inside this func
                l += 1
            while l < r and not self.alnum(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1 
        
        return True
        
    def alnum(self, ch):
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))