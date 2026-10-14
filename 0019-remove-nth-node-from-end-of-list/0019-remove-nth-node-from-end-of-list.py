# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
        
        temp=head
        ct=0
        while temp:
            ct+=1
            temp=temp.next
        if ct==n:
            return head.next
      
        i=1
        temp=head
        while i<ct-n and temp is not None:
            temp=temp.next
            i+=1
        temp.next=temp.next.next
        return head
        