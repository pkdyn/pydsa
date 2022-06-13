class Solution:
    #n , 1
    def maxProfit(self, prices: List[int]) -> int:
        #buy low, sell high!
        l, r = 0, 1 #adjaent rather than opposite pointers
        maxpro = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                pro = prices[r] - prices[l]
                maxpro = max(maxpro, pro) #takes care of negative profit too
            else:
                l = r #l shifted to new lowest price index
            r += 1
            
        return maxpro
            
        