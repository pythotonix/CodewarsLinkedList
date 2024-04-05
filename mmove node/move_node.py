class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    if source == None:
        raise ValueError
    if source == None and dest ==None:
        raise ValueError
    head_dest=Node(source.data)
    head_dest.next=dest
    dest=head_dest
    source=source.next
    return Context(source, dest)
