class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums3=sorted(nums1)
        l=len(nums3)
        if l%2==0:
            a=nums3[(l-1)//2]
            b=nums3[(l-1)//2+1]
            res=(a+b)/2.0
            return res
        else:
            return nums3[(l-1)//2]
        