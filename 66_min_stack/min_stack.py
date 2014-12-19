class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if len(self.minstack) == 0 or x <= self.minstack[-1]:
            self.minstack.append(x)

    # @return nothing
    def pop(self):
        top = self.stack[-1]
        self.stack.pop()
        if top == self.minstack[-1]:
            self.minstack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.minstack[-1]

if __name__ == "__main__":
    minstack = MinStack()
    val = [5, 0, 1, 3, 2]
    for item in val:
        minstack.push(item)
    print minstack.stack
    print minstack.minstack
