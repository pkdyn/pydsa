class Solution:
    #n, 1
    #n is len(s2)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        #list to track alphabet count
        cnt1 = cnt2 = [0] * 26 #avoid cnt1 = cnt2 = [0]*26
        
        l = matches = 0 #matches keep tracks of no of alphabets with same count
        
        for i in range(len(s1)): #mapping alphabet values for first len(s1) alphabets
            cnt1[ord(s1[i]) - ord('a')] += 1 
            cnt2[ord(s2[i]) - ord('a')] += 1 
        
        for i in range(26): #chedking if we already got a permutation
            if cnt1[i] == cnt2[i]:
                matches += 1  
    
        for r in range(len(s1), len(s2)): #len(s1) already covered
            if matches == 26: 
                return True #a permutation of s1 found in first len(s1) chars of s2
            
            #sliding right ptr
            idx = ord(s2[r]) - ord('a')
            cnt2[idx] += 1
            if cnt2[idx] == cnt1[idx]:
                matches += 1
            elif cnt2[idx] == cnt1[idx] + 1: #sliding upped an alphabet count by 1
                matches -= 1 #decrement matches
            
            #sliding left ptr
            idx = ord(s2[l]) - ord('a')
            cnt2[idx] -= 1
            if cnt2[idx] == cnt1[idx]:
                matches += 1
            elif cnt2[idx] == cnt1[idx] - 1: #sliding downed an alphabet's count by 1
                matches -= 1 #decrement matches
            l += 1 #increment left ptr
            
        return matches == 26