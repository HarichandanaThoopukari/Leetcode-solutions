class MinStack(object):

    def __init__(self):
        self.Minstack=[]
        self.stack=[]
        

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        
        self.stack.append(value)
        if not self.Minstack or value<=self.Minstack[-1]:
            self.Minstack.append(value)
       
        

    def pop(self):
        """
        :rtype: None
        """
        val=self.stack.pop()
        if val==self.Minstack[-1]:
            self.Minstack.pop()
        
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.Minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()