
class LinkedList:
    def __init__(self):
        self.data = 0
        self.next = None

def reversePrint(head):
    node = head
    res = []
    while node != None:
        res.append(node.data)
        node = node.next
    for index in range(len(res) - 1, -1, -1):
        print(res[index])


node1 = LinkedList()
node1.data = 1
node2 = LinkedList()
node2.data = 2
node2.next = node1
node3 = LinkedList()
node3.data = 3
node3.next = node2
node4 = LinkedList()
node4.data = 4
node4.next = node3
node5 = LinkedList()
node5.data = 5
node5.next = node4
reversePrint(node5)