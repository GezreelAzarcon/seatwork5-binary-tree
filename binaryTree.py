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
#IN ORDER TRAVERSAL (Left, Root, Right)
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

#PRE ORDER TRAVERSAL (Root, Left, Right)
    def preOrderTraversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preOrderTraversal()
        if self.right:
            elements += self.right.preOrderTraversal()
        
        return elements

#POST ORDER TRAVERSAL (Left, Right, Root)
    def postOrderTraversal(self):
        elements = []
        if self.left:
            elements += self.left.postOrderTraversal()
        if self.right:
            elements += self.right.postOrderTraversal()
        elements.append(self.data)

        return elements
    
#Minimum and Maximum methods
    def findMin(self):
        currentRoot = self
        while currentRoot.left:
            currentRoot = currentRoot.left
        print("The minimum element of the tree is: " + str(currentRoot.data))
    
    def findMax(self):
        currentRoot = self
        while currentRoot.right:
            currentRoot = currentRoot.right
        print("The maximum element of the tree is: " + str(currentRoot.data))
        
#Create a method for building the actual binary tree
def buildTree(elements):
    print("Building tree with these elements:",elements)
    root = BinaryTree(elements[0])

    for i in range(1,len(elements)):
        root.addNode(elements[i])

    return root


#myName = ["G","E","Z","R","E","E","L","A","Z","A","R","C","O","N"]
#myNameTree = buildTree(myName)
#print(myNameTree.postOrderTraversal())

numbers = [2, 12, 14, 42, 3, 31, 3, 11, 65, 10]
numbersTree = buildTree(numbers)

numbersTree.findMax()

numbersTree.findMin()



