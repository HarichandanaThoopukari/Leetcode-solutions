class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid=len(nums)//2
        ct=0
        for i in range(len(nums)):
            ct+=abs(nums[i]-nums[mid])
        return ct
           