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


# Questions:
# How do we handle an empty list?


# Head should point to none, then the next node should point to head.
# Have something to keep track of next, then replace next with the previous. Prev becomes current. Current becomes the saved next node.
# Return the previous

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

# O(n) for time because you iterate through the list. 
# O(1) for space, it will be just as long.