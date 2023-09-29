# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.\
    nodes = []
    cur = head
    while cur:
        nodes.append(cur.value)
        cur = cur.next

    if k == len(nodes):
        head.value = head.next.value
        head.next = head.next.next
        return head
    else:
        remove_idx = len(nodes) - k
    cur = head
    while cur:
        if cur.next and cur.next.value == nodes[remove_idx]:
            cur.next = cur.next.next
            break
        else:
            cur = cur.next
    pass
