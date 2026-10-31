class MinStack:

    def __init__(self):
        self.array = []
        self.minstack = []
        

    def push(self, value: int) -> None:
        self.array.append(value)
        if not self.minstack:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value, self.minstack[-1]))
        
        

    def pop(self) -> None:
        del self.array[-1]
        del self.minstack[-1]
        

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()