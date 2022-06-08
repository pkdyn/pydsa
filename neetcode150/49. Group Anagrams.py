class Solution:
    #n * avg len of each str, n
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list) #dict to hold list values
        
        for s in strs:
            count = [0] * 26 #alphabet count for every string
            
            for ch in s:
                count[ord(ch) - ord('a')] += 1
                
            res[tuple(count)].append(s) #immutable key
        
        return res.values()
        
                