class Solution(object):
    def zeroFilledSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct=0
        res=0
        for i in range(len(nums)):
            if nums[i]==0:
                ct+=1
                res+=ct
            else:
                ct=0
        return res