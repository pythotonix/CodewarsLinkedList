# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def linked_list_from_string(s):
    if s=="None":
        return None
    lst=s.split(" -> ")
    lst=lst[::-1]
    cur=Node(int(lst[1]))
    for i in lst[2:]:
        cur=Node(int(i),cur)
    return cur