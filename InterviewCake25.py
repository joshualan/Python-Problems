"""This module contains solutions to problem 25 of Interview Cake."""

class LinkedListNode:
    """Simple implementation for linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

def kth_to_last_node(k, node):
    curr = node
    kth_to_last = node

    for _ in range(k-1):
        if not node:
            return None

        curr = curr.next

    while curr.next:
        kth_to_last = kth_to_last.next
        curr = curr.next

    return kth_to_last

# Create some nodes
nodes = []
for i in range(10):
    nodes.append(LinkedListNode(i))

    if i > 0:
        nodes[i-1].next = nodes[i]

# Second to last node is 8
assert kth_to_last_node(2, nodes[0]) is nodes[8]

# Fourth to last node is 6
assert kth_to_last_node(4, nodes[0]) is nodes[6]
