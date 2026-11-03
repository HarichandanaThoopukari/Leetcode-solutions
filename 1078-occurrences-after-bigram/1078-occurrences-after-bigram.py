class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        a=text.split()
        res=[]
        for i in range(len(a)-2):
            if a[i]==first and a[i+1]==second:
                res.append(a[i+2])
        return res

        
        