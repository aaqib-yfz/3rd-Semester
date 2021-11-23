class queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,items):
        self.items.insert(0,items)
        print(items)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
q = queue()
q.enqueue(4)
q.enqueue('dog')
print(q)
print(q.size())