class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack=[]
        for i in operations:
            
            if i=="+":
                s=stack[-1]+stack[-2]
                stack.append(s)
            elif i=="D":
                d=2*stack[-1]
                stack.append(d)
            elif i=="C":
                stack.pop()
            else:
                stack.append(int(i))
        total=0
        for i in stack:
            total+=i
        return total
        
       

        