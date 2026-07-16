class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = [float('inf')]

    def push(self, val: int) -> None:
        if val <= self.mini[-1]: #it starts empty, so can I do this
            self.mini.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mini[-1]:
            self.mini.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
