class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    def reverse_recursive(node):
        if node.next is None:
            return node
        else:
            new_head = reverse_recursive(node.next)
            node.next.next = node
            node.next = None
            return new_head
    return reverse_recursive(head)