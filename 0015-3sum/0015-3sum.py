class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=set()
        nums=sorted(nums)
        for key,num in enumerate(nums) : 
            
            i=num
        
            left=key+1
            right=len(nums)-1
            while left<right   :
                my_sum=nums[left]+nums[right]

                if my_sum==-i :
                    result.add((i,nums[left],nums[right])) 
                    left+=1
                    right-=1
                    
                elif my_sum<-i:
                    left+=1
                else  :
                    right-=1

        return [list(x) for x in result]
      
        
       