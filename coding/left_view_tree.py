class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def leftView(root):
    if not root:
        return
    queue=[root]
    res=[]
    while queue:
        n=len(queue)
        for i in range(n):
            curr = queue.pop(0)
            if i==0:   #if i==n-1 then it would give the right view of the tree
                res.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    return res


if __name__ == '__main__':

	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.right = Node(4)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.left.right = Node(8)

	print(leftView(root))