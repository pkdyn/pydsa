class Solution:
    #n, n
    def isValid(self, s: str) -> bool:
        stck = [] #stack is just list in py
        pMap = {")":"(", "]":"[", "}":"{"} # HashMap for prnts
        
        for c in s:
            if c in pMap: # c is a closing prnt
                #stack is non empty and top element is corresponding open prnt
                if stck and stck[-1] == pMap[c]: 
                    stck.pop() #paired up, pop em
                else:
                    return False #not valid pairs
            else:
                stck.append(c) #push open prnt into stack
        #making sure that stack is empty if all paired up
        return True if not stck else False #one-liner for if else in return
    