class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ct=0
        for i in range(len(nums)-1):
            s=abs(sum(nums[:i+1])-sum(nums[i+1::]))
            if s%2==0:
                ct+=1
        return ct
        