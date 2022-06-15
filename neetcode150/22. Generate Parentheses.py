class Solution:
    #nth catalan number
    #4**n/n**0.5, 4**n/n**0.5
    def generateParenthesis(self, n: int) -> List[str]:
        # if nop < n -> (
        #if ncs < nop -> )
        #if nop = ncs = n -> done!
        stck = [] #stack to keep track of prnts
        res = []
        
        def bcktrck (nop, ncs):
            if nop == ncs == n:
                #append all elements of current stack as a single string
                res.append("".join(stck)) 
                
            
            if nop < n:
                stck.append("(")
                bcktrck(nop + 1, ncs)
                stck.pop() #backtrack to other branch
            
            if ncs < nop:
                stck.append(")")
                bcktrck(nop, ncs + 1)
                stck.pop() #backtrack to other branch
            
        bcktrck(0, 0) #spark case
        return res