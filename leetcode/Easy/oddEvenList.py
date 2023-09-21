class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        odd = head 
        even = odd.next
        even_head = head.next

        while odd.next and even.next:
            temp = odd.next
            odd.next = temp.next
            odd = odd.next
            temp2 = even.next
            even.next = temp2.next
            even = even.next
        
        odd.next = even_head
        return head