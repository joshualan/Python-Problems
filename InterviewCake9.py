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

# So we're gonna do a depth first tree so we're gonna use a stack.
def is_bst(node):

    def helper(node, position, high_bound, low_bound):
        if position == "left" and node.value > high_bound:
            return False
        if position == "right" and node.value < low_bound:
            return False    
        elif node is None:
            return True

        return (helper(node.left, "left", node.value, low_bound) and
                helper(node.right, "right", high_bound, node.value))

    return (helper(node.left, "left", node.value, node.value) and
            helper(node.right, "right", node.value, node.value))
