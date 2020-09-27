class NodeCreate:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def insert(self,value):
        node=NodeCreate(value)
        if self.head is None:
            self.head=node
            return
        currNode=self.head
        while True:
            if currNode.nextNode is None:
                currNode.nextNode=node
                break
            currNode=currNode.nextNode



    def printLL(self):
        currNode=self.head
        while currNode is not None:
            print(currNode.value, end=' ')
            currNode=currNode.nextNode
        #print "None"

    def takeLast(self):
        currNode=LL.head
        while currNode.nextNode.nextNode is not None:
            currNode=currNode.nextNode

        RL.insert(currNode.nextNode.value)
        currNode.nextNode = None

    def Rev(self):
        cur1=LL.head
        cur2=RL.head
        while cur2.nextNode is not None:
            cur2=cur2.nextNode
        cur2.nextNode=cur1




LL=LinkedList()

LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)

LL.printLL()
print()
RL=LinkedList()
RL.takeLast()
RL.takeLast()
RL.takeLast()
RL.Rev()
RL.printLL()
