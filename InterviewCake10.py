class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

def find_second_largest(node):
    # If this is the only node, there is no second largest value
    if node.left is None and node.right is None:
        return None

    # Find the max node
    while (node.right):
        penultimate_node = node
        node = node.right

    # Find the second largest node
    if (node.left is not None):
        penultimate_node = node.left

        while (penultimate_node.right is not None):
            penultimate_node = penultimate_node.right

    return penultimate_node.value
