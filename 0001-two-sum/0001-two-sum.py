class Solution(object):
    def twoSum(self, nums, target):
       s={}
       for i in range(len(nums)):
          b=target-nums[i]

          if b in s:
            return [s[b],i]

          s[nums[i]]=i
         