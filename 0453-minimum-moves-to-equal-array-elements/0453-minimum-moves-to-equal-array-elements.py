class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=min(nums)
        s=0
        for i in range(len(nums)):
           s+=nums[i]-mini
        return s













        """
        nums.sort()
        ct=0
        for i in range(len(nums)):
            maxi=max(nums)
            for i in range(len(nums)):
                if nums[i]==maxi:
                    break
                nums[i]+=1
                ct+=1
            if nums.count(maxi)==len(nums):
                return ct"""


        