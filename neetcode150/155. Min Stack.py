class MinStack:
    #1, n
    def __init__(self):
        self.stck = []
        self.mnstck = [] #to keep track of min element

    def push(self, val: int) -> None:
        self.stck.append(val) #not push
        if self.mnstck: #if min stack not empty
            #new top = minimum of val and top of min stack 
            self.mnstck.append(min(val, self.mnstck[-1]))
        else:
            self.mnstck.append(val)

    def pop(self) -> None:
        self.stck.pop()
        self.mnstck.pop()

    def top(self) -> int:
        return self.stck[-1]
        

    def getMin(self) -> int:
        return self.mnstck[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()