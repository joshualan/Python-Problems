"""
This module contains solutions to problem 23 of Interview Cake.

So my solution takes O(1) space because hey, we only have variables.

Our runtime is O(n) though because the fast runner will never outpace the slow
one. Worst case scenario is the node at the end loops to the first. Let's take
a scenario of 5 nodes. Let's say slow runner takes 4 steps to be at the 5th
node. The fast runner starts at node 2 and takes 4*2=8 steps to be at the
10th->5th node. They'll always hit each other in O(n) time. 
"""

# I'm going to use dictionaries for my node implementation

def create_node(value):
    """Creates a node using a dictionary implementation."""
    return {"value": value, "next": None}

def contains_cycle(node):
    """Checks to see if there's a cycle in a singly-linked list"""
    if not node['next']:
        return False

    slow_runner = node
    fast_runner = node['next']

    while True:
        # No need to check slow_runner is fast_runner is ahead
        if not (fast_runner['next'] and fast_runner['next']['next']):
            return False
        if (fast_runner is slow_runner
                or fast_runner['next'] is slow_runner):
            return True

        slow_runner = slow_runner['next']
        fast_runner = fast_runner['next']['next']

a = create_node('a')
b = create_node('b')
c = create_node('c')
d = create_node('d')
e = create_node('e')
f = create_node('f')

a['next'] = b
b['next'] = c
c['next'] = d
d['next'] = b

e['next'] = f

assert contains_cycle(a) is True and contains_cycle(c) is True
assert contains_cycle(e) is False and contains_cycle(f) is False
