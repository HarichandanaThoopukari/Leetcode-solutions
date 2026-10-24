class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        ct=0
        for i in s:
            if i=="(":
                stack.append(i)
            elif stack and i==")":
                ct+=2
                stack.pop()
        return len(s)-ct