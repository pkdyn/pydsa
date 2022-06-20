class Solution:
    #n, n
    def largestRectangleArea(self, heights: List[int]) -> int:
        amx = 0
        stck = [] #[start idx, h]
        
        for i, h in enumerate(heights):
            strt = i #can be backextended but initially index itself
            while stck and stck[-1][1] > h: #current height is smaller than top of stack
                #area corresponding to stck top cant be extended till end
                topIdx, topHgt = stck.pop() #pop element that cant be extended
                amx = max(amx, topHgt*(i - topIdx)) #calcuate area related with popped element
                strt = topIdx #back-extend start of current height to index of popped element 
            stck.append([strt, h]) #append height and start index of current height
            
        for i, h in stck:
            amx = max(amx, h*(len(heights) - i)) 
            #area of elements in stack extend to the end:len(heigths) - strt
        
        return amx