# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

            

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create a dummy node
        prev, cur = None, head

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev



# Head should point to none, then the next node should point to head. 

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        return prev