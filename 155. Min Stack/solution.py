class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value: int) -> None:
        # lets push every value into the normal stack
        self.stack.append(value)

        # pushing into min_stack if
        # min_stack is empty, value is <= current min in min_stack
        if not self.min_stack or self.min_stack[-1] >= value:
            self.min_stack.append(value)

    def pop(self) -> None:
        # store the popped value
        v = self.stack.pop()

        # if the popped value is also the current min we remove it from the min_stack as well
        if v == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # return top of normal stack
        return self.stack[-1]


    def getMin(self) -> int:
        # current min is always top of min_stack
        return self.min_stack[-1]
