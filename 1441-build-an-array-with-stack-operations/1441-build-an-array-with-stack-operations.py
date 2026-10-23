class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        s=[]
        j=0
        for i in range(1,n+1):
            if j==len(target):
                break
           
            if i in target:
                s.append("Push")
                j+=1
            else:
                s.append("Push")
                s.append("Pop")
        return s