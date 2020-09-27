class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None

def top_view(root):
    if not root:
        return
    queue=[]
    res={}
    queue.append(root)
    root.hd=0
    while queue:
        curr=queue.pop(0)                   ###########################################
        if curr.hd not in res:              #for bottom view just remove this condtion#
            res[curr.hd] = curr.val         #     we have to update mappings for      #
        if curr.left:                       #       for each new value of HD          #
            curr.left.hd=curr.hd-1          ###########################################
            queue.append(curr.left)
        if curr.right:
            curr.right.hd = curr.hd+1
            queue.append(curr.right)
    print(sorted(res.items()))
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.right.left = Node(5)
	root.right.right = Node(6)
	root.right.left.left = Node(7)
	root.right.left.right = Node(8)

top_view(root)