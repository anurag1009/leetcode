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
            print currNode.value,"->",
            currNode=currNode.nextNode
        print "None"


    def revList(self):
        if self.head is None:
            print "None"
        else:
            #nxtBlock=None
            prev=None
            currNode=self.head
            while currNode:
                nxtBlock=currNode.nextNode
                currNode.nextNode=prev
                prev=currNode
                currNode=nxtBlock
            self.head=prev

LL=LinkedList()

LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.printLL()
LL.revList()
LL.printLL()