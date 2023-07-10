class MinStack:

    def __init__(self):
        self.list = []
        self.min_vals = []
        

    def push(self, val: int) -> None:
        self.list.append(val)
        if len(self.min_vals) == 0:
            self.min_vals.append(val)
        elif self.min_vals[-1] >= val:
            self.min_vals.append(val)

    def pop(self) -> None:
        removed = self.list.pop()
        if removed == self.min_vals[-1]:
            self.min_vals.pop()

    def top(self) -> int:
        return self.list[-1] if self.list else None

    def getMin(self) -> int:
        return self.min_vals[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()