# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    nodes = []
    node_number = 0
    cur = linkedList
    
    while cur:
        node_number += 1
        nodes.append(cur.value)
        cur = cur.next

    cur = linkedList
    middle_node = nodes[len(nodes) // 2]

    while cur:
        if cur.value == middle_node:
            return cur
        cur = cur.next
