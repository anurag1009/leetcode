class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def max_depth(node):
    if node is None:
        return 0
    else:
        ldepth=max_depth(node.left)
        rdepth=max_depth(node.right)

        if(ldepth>rdepth):
            return ldepth+1
        else:
            return rdepth+1

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.right=Node(5)

print(max_depth(root))

