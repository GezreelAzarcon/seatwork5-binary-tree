#Create a binary tree class
class BinaryTree:
    #Create a method for __init__ with main class variables
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Create a method for adding a new node
    def addNode(self, data):
        #to prevent copies
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addNode(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addNode(data)
            else:
                self.right = BinaryTree(data)

#Create a traversal method/s for sorting the nodes
#IN ORDER TRAVERSAL
    def inOrderTraversal(self):
        elements = []
        #left
        if self.left:
            elements += self.left.inOrderTraversal()
        #root
        elements.append(self.data)
        #right
        if self.right:
            elements += self.right.inOrderTraversal()
        
        return elements

#PRE ORDER TRAVERSAL
    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        
        return elements

#POST ORDER TRAVERSAL
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)

        return elements
        
#Create a method for building the actual binary tree
def buildTree(elements):
    print("Building tree with these elements:",elements)
    root = BinaryTree(elements[0])

    for i in range(1,len(elements)):
        root.addNode(elements[i])

    return root


countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
numbers = [7, 5, 12, 3, 6, 4, 13, 8]
numbersTree = buildTree(numbers)
print(numbersTree.postOrderTraversal())
