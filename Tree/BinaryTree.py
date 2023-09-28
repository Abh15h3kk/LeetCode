import QueueLinkedList as queue

class TreeNode:
    def __init__ (self,data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootnode):
    if rootnode is None:
        return
    print(rootnode.data)
    preOrderTraversal(rootnode.leftChild)       # Time complexity is O(N) and Space complexity is O(N)
    preOrderTraversal(rootnode.rightChild)

def inOrderTraversal(rootnode):
    if rootnode is None:
        return
    inOrderTraversal(rootnode.leftChild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightChild)

def postOrderTraversal(rootnode):
    if rootnode is None:
        return
    postOrderTraversal(rootnode.leftChild)
    postOrderTraversal(rootnode.rightChild)
    print(rootnode.data)

def levelOrderTraversal(rootnode):
    if rootnode is None:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode,nodeValue):
    if rootNode is None:
        return 'BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return 'Node is present in BT'
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return 'Node not found'

def insertNodeBT(rootNode,newNode):
    if rootNode is None:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return 'Inserted'
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return 'inserted'

def getDeepestNodeBT(rootnode):
    if rootnode is None:
        return 'BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
    
def deleteDeepestNodeBT(rootnode,deepestNode):
    if rootnode is None:
        return 'BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value == deepestNode:
                root.value = None
                return
            if root.value.leftChild is not None:
                if root.value.leftChild == deepestNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                if root.value.rightChild == deepestNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)

def deleteNodeBT(rootNode,nodedata):
    if rootNode is None:
        return 'BT does not exist'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        deepestNode = getDeepestNodeBT(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == nodedata:
                deepestNode = getDeepestNodeBT(rootNode)
                root.value.data = deepestNode.data
                deleteDeepestNodeBT(rootNode,deepestNode)
                return 'Successfully deleted'
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return 'Failed to delete'
        
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return 'BT successfully deleted'

BT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
BT.leftChild = leftChild
BT.rightChild = rightChild
Tea = TreeNode('Tea')
Coffee = TreeNode('Coffee')
leftChild.leftChild = Tea
leftChild.rightChild = Coffee
Coca = TreeNode('Coca')

deleteNodeBT(BT,'Hot')
levelOrderTraversal(BT)
