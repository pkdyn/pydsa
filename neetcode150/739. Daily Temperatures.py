class Solution:
    #n, n
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures) #initialize with zeroes
        stck = [] #[tmp, i]
        
        for i, tmp in enumerate(temperatures):
            while stck and tmp > stck[-1][0]:#tmp is greater than temp value at stack top
                tmptop, itop = stck.pop() #initialize variavles with pop()
                res[itop] = i - itop 
            stck.append([tmp, i]) #empty stack or lower tmp
        
        return res