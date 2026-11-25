class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res=[]
        ans=[]

        for num in arr2:
            for x in arr1:
                if x==num:
                    res.append(x)
        for x in arr1:
            if x not in arr2:
                ans.append(x)
        ans.sort()

        return res+ans
       

        