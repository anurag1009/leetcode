class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList:
    def __init__(self,head=None):
        self.head=head

    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        else:
            currNode=self.head
        while currNode.nextNode is not None:
            currNode=currNode.nextNode
        currNode.nextNode=node

    def insert_At_N(self,data,pos):
        node=Node(data)
        if self.head is None:
            self.head=node
            return
        else:
            currNode=self.head
            i=1
            while i!=pos-1:
                currNode=currNode.nextNode
                i+=1
            node.nextNode=currNode.nextNode
            currNode.nextNode=node
    def delt_At_N(self,pos):
        currNode=self.head
        if pos==1:
            self.head=currNode.nextNode
        else:
            i=1
            while i!=pos-1:
                currNode=currNode.nextNode
                i+=1
            currNode.nextNode=currNode.nextNode.nextNode

    def  reverse_list(self):
        prev=None
        currNode=self.head
        while currNode is not None:
            Next=currNode.nextNode
            currNode.nextNode=prev
            prev=currNode
            currNode=Next
        self.head=prev


    def printLL(self):
        currrNode=self.head
        while currrNode is not None:
            print(currrNode.data,"->",end=" ")
            currrNode=currrNode.nextNode
        print("None")

l=list(map(int,input().split()))
LL=LinkedList()
for i in l:
    LL.insert(i)
LL.printLL()

LL.insert_At_N(5,3)
LL.printLL()

LL.delt_At_N(5)
LL.printLL()

LL.reverse_list()
LL.printLL()

