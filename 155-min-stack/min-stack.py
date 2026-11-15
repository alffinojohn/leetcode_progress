class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if not self.stack:
            self.stack.append((value,value))
        else:
            minVal = self.stack[-1][1]
            if minVal > value:
                minVal = value
            self.stack.append((value, minVal))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


    