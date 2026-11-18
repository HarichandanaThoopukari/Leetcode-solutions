class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        ans=float('inf')
        n=len(nums)

        for i in range(n):
            s=0

            for j in range(i, min(i+r,n)):
                s+=nums[j]

                if j-i+1>=l and s>0:
                    ans=min(ans,s)

        return -1 if ans==float('inf') else ans
        
        