# Linked Lists - Alternating Split

# Write an AlternatingSplit() function that takes one list and divides up its nodes to make two smaller lists. The sublists should be made from alternating elements in the original list. So if the original list is a -> b -> a -> b -> a -> null then one sublist should be a -> a -> a -> null and the other should be b -> b -> null.

# list = 1 -> 2 -> 3 -> 4 -> 5 -> None
# alternating_split(list).first == 1 -> 3 -> 5 -> None
# alternating_split(list).second == 2 -> 4 -> None
# For simplicity, we use a Context object to store and return the state of the two linked lists. A Context object containing the two mutated lists should be returned by AlternatingSplit().

# If the passed in head node is null/None/nil or a single node, throw an error.
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None:
        raise ValueError
    if head.next is None:
        raise ValueError
    nodes = Context(head, head.next)
    probe = head
    curr = head.next
    while curr:
        probe.next = curr.next
        probe = curr.next
        if probe:
            curr.next = probe.next
            curr = probe.next
        else:
            return nodes
    return nodes