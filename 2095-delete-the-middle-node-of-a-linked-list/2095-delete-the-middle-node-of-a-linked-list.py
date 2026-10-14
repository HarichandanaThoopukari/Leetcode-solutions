# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        ct=0
        temp=head
        while temp:
            ct+=1
            temp=temp.next
       
        mid=ct//2
        i=0
        temp=head
        while i<mid-1 and temp is not None:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        return head

       