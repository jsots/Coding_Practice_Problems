class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
            
        cur = head
        count = 0

        while cur:
            cur = cur.next
            count += 1
        
        remove_idx = count // 2
        count = 0
        cur = head

        while cur:
            count += 1
            if count == remove_idx:
                cur.next = cur.next.next   
            else:
                cur = cur.next
            
        return head