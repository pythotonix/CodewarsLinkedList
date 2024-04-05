# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    count=0
    while node:
        if count == index:
            return node
        count +=1
        node = node.next
    raise IndexError