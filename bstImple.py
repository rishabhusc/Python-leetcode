class node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

class LinkedList:
    def __init__(self):
        self.root=None

    def append(self,value):
        if self.root is None:
            self.root=node(value)

        else:
            self._append(value,self.root)

    def _append(self,value,cur):
        if value<cur.value:
            if cur.left is None:
                cur.left=node(value)
                cur.left.parent=cur
            else:
                self._append(value,cur.left)
        elif value>cur.value:
            if cur.right is None:
                cur.right=node(value)
                cur.right.parent=cur
            else:
                self._append(value,cur.right)
        else:
            print("Aaww value already present in Tree !! ")

    def print(self):
        if self.root!=None:
            self._print(self.root)
        else:
            return


    def height(self):
        if self.root is None:
            return 0
        else:
            return  self._height(self.root,0)


    def _height(self,cur,cur_height):
        if cur is None:
            return cur_height
        leftHeight=self._height(cur.left,cur_height+1)
        rightHeight=self._height(cur.right,cur_height+1)
        return max(leftHeight,rightHeight)

    def _print(self,cur):
        if cur:
            self._print(cur.left)
            print(cur.value,end=" ")
            self._print(cur.right)

    def serach(self,valeuToSearch):
        if self.root is None:
            return False
        else:
            return self._search(self.root,valeuToSearch)
    def _search(self,cur,valueToSeacrh):
        if cur.value==valueToSeacrh:
            return True
        elif valueToSeacrh<cur.value and cur.left!=None:
            return self._search(cur.left,valueToSeacrh)
        elif valueToSeacrh>cur.value and cur.right!=None:
            return self._search(cur.right,valueToSeacrh)
        else:
            return False
    def preOrder(self):
        if self.root is None:
            return
        else:
            self._preOrder(self.root)

    def _preOrder(self,cur):
        if cur:
            print(cur.value,end=" ")
            self._preOrder(cur.left)
            self._preOrder(cur.right)

    def find(self,value):
        if self.root is None:
            return
        else:
            return self._find(self.root,value)

    def _find(self,cur,value):
        if cur.value==value:
            return cur
        elif value<cur.value and cur.left!=None:
            return self._find(cur.left,value)
        elif value>cur.value and cur.right!=None:
            return self._find(cur.right,value)

    def levelOrder(self):
        if self.root is None:
            return
        l=list()
        l.append(self.root)
        lw=[]
        while len(l)>0:
            lw.append(l[-1].value)
            n=l.pop()
            if n.left:
                l.insert(0,n.left)
            if n.right:
                l.insert(0,n.right)
        return lw










ll=LinkedList()
ll.append(2)
ll.append(1)
ll.append(3)
ll.append(7)
ll.append(4)
ll.print()
print('Height -',ll.height())
print("Value to be searched 11",ll.serach(11))
print("Value to be searched 5",ll.serach(5))
ll.preOrder()
print("")
print(ll.levelOrder())

