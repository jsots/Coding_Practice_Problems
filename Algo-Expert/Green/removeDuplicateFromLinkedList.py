# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    cur = linkedList
    while cur:
        if cur.next and cur.next.value == cur.value:
            cur.next = cur.next.next
        else:
            cur = cur.next
            
    return linkedList
