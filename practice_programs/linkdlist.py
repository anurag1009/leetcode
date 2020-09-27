class NodeCreate:
    def __init__(self,value,nextNode=None):
        self.value=value
        self.nextNode=nextNode

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def insertAtN(self,value,pos):
        node=NodeCreate(value)
        if self.head is None:
            self.head=node
            return
        else:
            currNode = self.head
            i = 0
            while i<pos:
                if(i==pos-1):
                    node.nextNode=currNode.nextNode
                    currNode.nextNode=node
                currNode = currNode.nextNode
                i+=1

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
            print(currNode.value,"->", end=' ')
            currNode=currNode.nextNode
        print("None")

l=list(map(int,input().split()))
LL=LinkedList()

for i in l:
    LL.insert(i)

LL.printLL()
LL.insertAtN(7,2)
LL.printLL()

#program to create LInkedList in Python

"""class NodeCreate:
    def __init__(self,data,nextNode=None):
        self.data=data
        self.nextNode=nextNode

node1=NodeCreate("1")
node2=NodeCreate("2")
node3=NodeCreate("3")

node1.nextNode=node2 #we are assigning the address of node2 in the "link" field of node1
node2.nextNode=node3
print(node2) #if we print node2 which is the obj. of class it will show its addr.
print(getattr(node1,'nextNode')) #same getatrr() method also shows the addr. of a particular attribute of class

currNode=node1
while currNode.nextNode!=None:
    print currNode.data,"->" ,
    currNode=currNode.nextNode
print currNode.data
"""
