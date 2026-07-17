class MinStack:

    def __init__(self):
        self.Stack=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.Stack.append(val)
        
        if self.minStack and self.minStack[-1]<val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.Stack:
            self.Stack.pop()
            self.minStack.pop()

    def top(self) -> int:
        return self.Stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]