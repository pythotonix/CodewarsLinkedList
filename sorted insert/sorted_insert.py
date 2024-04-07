""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    if head is None:
        return Node(data)
    probe = head
    if head.data>data:
        head = Node(data)
        head.next=probe
        return head
    while probe!=None:
        if probe.data<data-0.5:
            probe=probe.next
        else:
            probe_new = Node(data)
            probe_new.next=probe.next
            probe.next=probe_new
            break
    return head