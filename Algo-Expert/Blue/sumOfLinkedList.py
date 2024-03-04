# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    list_one = []
    list_two = []

    cur_1 = linkedListOne
    cur_2 = linkedListTwo

    while cur_1:
        list_one.append(cur_1.value)
        cur_1=cur_1.next
    while cur_2:
        list_two.append(cur_2.value)
        cur_2=cur_2.next

    # int_1 = ''.join(list_one)
    
    return list_one

print(sumOfLinkedLists(linkedListOne, linkedListTwo))