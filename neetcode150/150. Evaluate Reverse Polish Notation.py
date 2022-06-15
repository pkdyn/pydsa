class Solution:
    #n, n
    def evalRPN(self, tokens: List[str]) -> int:
        stck = []
        for ch in tokens:
            if ch == "+":
                a, b = stck.pop(), stck.pop()
                stck.append(a + b) 
            elif ch == "-":
                a, b = stck.pop(), stck.pop()
                stck.append(b - a) #second ele op first ele for - and /
            elif ch == "*":
                a, b = stck.pop(), stck.pop()
                stck.append(a * b)
            elif ch == "/": 
                a, b = stck.pop(), stck.pop()
                stck.append(int (b / a))
                #negative // moves away from 0
                #postitive // moves towards zero
                #int() truncates whatever decimal
            else: 
                stck.append(int(ch))
        return stck[0] #dont forget to return the final result in stck!