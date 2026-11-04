class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        s = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i!=j and j!=k and i!=k:
                        if digits[i]!=0 and digits[k]%2==0:
                            num=digits[i]*100+digits[j]*10+digits[k]
                            s.add(num)

        return len(s)
       
            
