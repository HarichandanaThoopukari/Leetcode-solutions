class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxi=max(nums)
        ct=0
        for i in range(len(nums)):
            ct+=abs(maxi-nums[i])
        return ct