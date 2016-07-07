class MaxStack:

    # initialize an empty list
    def __init__(self):
        self.items = []
        self.max_stack = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

        if item > self.get_max():
            self.max_stack.append(item)

    # remove the last item
    def pop(self):

        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items: return None

        if self.peek() == self.get_max():
            self.max_stack.pop() 

        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items: return None
        return self.items[len(self.items)-1]

    def get_max(self):
        if not self.max_stack: return None
        return self.max_stack[len(self.max_stack)-1]

