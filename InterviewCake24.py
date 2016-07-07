"""This module contains solutions to problem 24 of Interview Cake."""

class LinkedListNode:
    """Simple implementation for linked list."""

    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_list(node):
    curr = node
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev

        prev = curr
        curr = nxt

# Create some nodes
nodes = []
for i in range(6):
    nodes.append(LinkedListNode(i))

    if i > 0:
        nodes[i-1].next = nodes[i]

reverse_list(nodes[0])
assert nodes[0].next is None
assert nodes[5].next is nodes[4]
