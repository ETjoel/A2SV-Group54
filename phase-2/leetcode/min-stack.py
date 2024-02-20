class MinStack:

    def __init__(self):
        self.stk = []

    def push(self, val: int) -> None:
        if self.stk:
            self.stk.append((val, min(val, self.stk[-1][1])))
        else:
            self.stk.append((val, val))

    def pop(self) -> None:
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1][0]

    def getMin(self) -> int:
        return self.stk[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()