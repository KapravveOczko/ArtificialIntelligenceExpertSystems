class Queue:

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)

    def print_queue(self):
        print('\n'.join(map(str, self.items)) + '\n')
