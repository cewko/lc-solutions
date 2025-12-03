class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        minimum = min(value, self.min_stack[-1] if self.min_stack else value)
        self.min_stack.append(minimum)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self):
        return self.stack[-1]
        
    def getMin(self):
        return self.min_stack[-1]
