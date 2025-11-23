class FilaDePrioridadeManual:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.items.sort()   

    def poll(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
