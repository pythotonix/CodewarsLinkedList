def loop_size(node):
    tortoise = node
    hare = node.next
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next.next
    size = 1
    hare = hare.next
    while tortoise != hare:
        hare = hare.next
        size += 1

    return size