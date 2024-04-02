def stringify(node):
    if node is None:
        return "None"
    else:
        s=''
        probe = node
        while probe is not None:
            if probe.next is not None:
                s+=str(probe.data)+" -> "
            else:
                s+=str(probe.data)
            probe = probe.next
        return s+" -> None"