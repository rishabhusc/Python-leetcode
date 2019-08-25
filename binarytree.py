class Node:
    def __init__(self,value):
        self.value=value
        self.leftChild=None
        self.rightChild=None
class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    '''
        Function for preorder:
        Flow - Root->Left->Right
    '''
    def printTree(self,printType):
        if printType=="preorder":
            return self.preOrderTraversal(self.root,"")
        elif printType=="inorder":
            return self.inorderTraversal(self.root,"")
        elif printType=="postorder":
            return self.postOrder(self.root,"")

    def preOrderTraversal(self,start,traversal):
        if start:
            traversal+= str(start.value)+" - "
            traversal = self.preOrderTraversal(start.leftChild,traversal)
            traversal = self.preOrderTraversal(start.rightChild,traversal)
        return traversal

    def postOrder(self,start,traversal):
        if start:

            traversal=self.postOrder(start.leftChild,traversal)
            traversal=self.postOrder(start.rightChild,traversal)
            traversal+=str(start.value)+" - "
        return traversal


    def inorderTraversal(self,start,traversal):
        if start:
            traversal = self.inorderTraversal(start.leftChild,traversal)
            traversal+= str(start.value)+" - "
            traversal = self.inorderTraversal(start.rightChild,traversal)
        return traversal






tree=BinaryTree(1)
tree.root.leftChild=Node(2)
tree.root.rightChild=Node(3)
tree.root.leftChild.leftChild=Node(4)

tree.root.leftChild.rightChild=Node(5)
tree.root.rightChild.leftChild=Node(6)
tree.root.rightChild.rightChild=Node(7)

print(tree.printTree("preorder"))
print(tree.printTree("inorder"))
print(tree.printTree("postorder"))




