class Solution:
    #n, n
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        window, Tcnt = {}, {} #hashTables to track char count
        
        for c in t:
            Tcnt[c] = 1 + Tcnt.get(c, 0) #map t's char count
        
        l = 0
        #res cant be empty!
        res = [0]*2 #list of two zeros as placeholders for window pointers
        resLen = float("infinity") #for min commparisons
        have, need = 0, len(Tcnt) #variable to track reqd char count
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)
            
            if ch in Tcnt and window[ch] == Tcnt[ch]:
                have += 1 #count of one of the reqd char satisfied
            
            while have == need:
                if r - l + 1 < resLen: #update res
                        res = [l, r]
                        resLen = r - l + 1
                window[s[l]] = -1 + window.get(s[l], 0) #trying to get a smaller substring
                if s[l] in Tcnt and window[s[l]] < Tcnt[s[l]]: #less than and not equal to
                    have -= 1
                l +=1
        a, b = res
        return s[a: b + 1] if resLen < float("infinity") else "" 
        #return empty string if no substring