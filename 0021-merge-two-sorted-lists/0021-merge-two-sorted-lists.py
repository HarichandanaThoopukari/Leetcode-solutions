# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1=[]
        l2=[]
        temp1=list1
        while temp1:
            l1.append(temp1.val)
            temp1=temp1.next
        temp2=list2
        while temp2:
            l2.append(temp2.val)
            temp2=temp2.next
        l1.extend(l2)
        l1.sort()

        dummy=ListNode(0)
        cur = dummy

        for num in l1:
            cur.next=ListNode(num)
            cur=cur.next

        return dummy.next
            
