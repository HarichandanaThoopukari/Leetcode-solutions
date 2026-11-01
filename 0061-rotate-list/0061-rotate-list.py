# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        k=k%n


        while k!=0:
            temp=head
            prev=None
            while temp.next:
                prev=temp
                temp=temp.next
            prev.next=None
            temp.next=head
            head=temp
            k-=1
        return head

        

        