class Stack:

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def print_stack(self):
        print('\n'.join(map(str, self.items)) + '\n')