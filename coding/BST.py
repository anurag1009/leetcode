class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.traverse(data,self.root)

    def traverse(self,data,curr_node):

        if data>curr_node.data:
            if curr_node.right==None:
                curr_node.right=Node(data)
            else:
                self.traverse(data,curr_node.right)
        elif data<curr_node.data:
            if curr_node.left==None:
                curr_node.left=Node(data)
            else:
                self.traverse(data,curr_node.left)
        else:
            print("Value already exists!!!")


    def find(self,data):
        if self.root:
            found=self._search(data,self.root)
            if found:
                return True
            return False
        else:
            return None

    def _search(self,data,curr_node):
        if data>curr_node.data and curr_node.right:
            return self._search(data, curr_node.right)
        elif data>curr_node.data and curr_node.right:
            return self._search(data, curr_node.right)
        if data == curr_node.data:
            return True

bst=BST()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(10)
bst.insert(5)
bst.insert(1)

print(bst.find(8))


