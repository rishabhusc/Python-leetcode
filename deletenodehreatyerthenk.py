class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.root=None

    def append(self,value):
        if self.root is None:
            self.root=Node(value)
            return
        cur=self.root
        while cur.next:
            cur=cur.next
        cur.next=Node(value)

    def removeelemGeeyteerThan(self,k):
        if self.root is None:
            return
        prev=None
        cur=self.root
        while cur:
            if cur.value>k:
                prev.next=cur.next
                cur=None

            prev=cur
            cur=prev.next
    def print(self):
        cur=self.root
        while cur:
            print(cur.value)
            cur=cur.next




ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.removeelemGeeyteerThan(3)
ll.print()