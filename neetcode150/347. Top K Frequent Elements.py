class Solution:
    #n, n
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        count = [[] for i in range(len(nums) + 1)] #array of 0 to n empty arrays
        #bucket sort
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)
            
        for n, c in freq.items(): #items(): enumerate() but for dict
            count[c].append(n)    #count's index stores freq
            #value stores list of elements with that freq
            
        res = []
        #traversing array in reverse order
        for i in range(len(count) - 1, 0, -1): #0th index value ignored (bcauz zero freq elements)
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return               
            
            