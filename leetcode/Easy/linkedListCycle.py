# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Are all the values unique?
        seen = set()
        if not head:
            return False

        while head:
            if head in seen:
                return True
            seen.add(head)
            nxt = head.next
            head = nxt
        
        return False