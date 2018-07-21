class Stack(object):
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def len(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]


s=Stack()
s.push(1)
s.push("ssds")
s.push(True)
print(s.len())
print(s.pop())

