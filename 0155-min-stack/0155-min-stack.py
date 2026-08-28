class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = []
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)

        if self.minimum:
            self.minimum.append(min(value, self.minimum[-1]))
        else:
            self.minimum.append(value)
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minimum.pop()

        

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()