class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        m=0
        for i in s:
            if i=="(":
                stack.append(i)
                res=len(stack)
                if res>m:
                    m=res
               
            elif i==")":
                stack.pop()
        return m
        

        