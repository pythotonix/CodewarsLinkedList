class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    dummy = Node(head)
    current = dummy
    while current.next and current.next.next:
        first = current.next
        second = current.next.next
        first.next = second.next
        current.next = second
        second.next = first
        current = current.next.next
    return dummy.next