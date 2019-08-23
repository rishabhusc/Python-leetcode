class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def getStack(self):
        return self.items
    def isEmpty(self):
        return self.items==[]
    def isPeek(self):
        if not self.isEmpty():
            return self.items[-1]
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(s.getStack())
s.pop()
print(s.getStack())
print("Is empty : ",s.isEmpty())
print(s.isPeek())