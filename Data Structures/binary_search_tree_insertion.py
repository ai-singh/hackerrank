class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
    def insert(self, val):
        #Enter you code here.
        if not self.root:
            self.root = Node(val)
            return self.root
        ref = self.root
        while True:
            if val > ref.info:
                if ref.right:
                    ref = ref.right
                else:
                    ref.right = Node(val)
                    break
            else:
                if ref.left:
                    ref = ref.left
                else:
                    ref.left = Node(val)
                    break
        return self.root




node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node4.right = node7
node4.left = node2
node2.left = node1
node2.right = node3
b = BinarySearchTree()
b.root = node4
b.insert(6)