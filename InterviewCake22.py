"""This module contains solutions to the 22nd problem of Interview Cake."""

class LinkedListNode:
    """Simple class to represent a linked list"""
    def __init__(self, value):
        self.value = value
        self.next = None

    def delete_node(self):
        """Deletes a node in O(1). Has pretty bad side-effects."""
        if self.next:
            self.value = self.next.value
            self.next = self.next.next
        else:
            raise Exception("Can't delete the last node unfortunately.")

    def add_next(self, node):
        """Adds the next node in the list"""
        self.next = node

node_a = LinkedListNode('A')
node_b = LinkedListNode('B')
node_c = LinkedListNode('C')

node_a.add_next(node_b)
node_b.add_next(node_c)

node_b.delete_node()
