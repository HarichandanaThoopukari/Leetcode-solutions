class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        ans=[]
        for i in digits:
            s+=str(i)
        res=(int(s)+1)
        for i in str(res):
            ans.append(int(i))
        return ans


        