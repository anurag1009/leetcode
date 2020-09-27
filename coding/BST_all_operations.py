class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def insert(root,val):
    if root is None:
        return Node(val)
    if val<root.data:
        root.left=insert(root.left,val)
    else:
        root.right=insert(root.right,val)
    return root

def inorder(root):
    if root is None:
        return root
    else:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def minValueNode(root):
    if root.left is None:
        return root
    else:
       return minValueNode(root.left)

def deltNode(root,val):
    if root is None:
        return root
    if val<root.data:
        root.left=deltNode(root.left,val)
    elif val>root.data:
        root.right=deltNode(root.right,val)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        if root.right is None:
            temp=root.right
            root=None
            return temp
        else:
            temp=minValueNode(root.right)
            root.data=temp.data
            root.right = deltNode(root.right, temp.data)
    return root


root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print("Inorder traversal of the given tree")
inorder(root)

print("\nDelete 20")
root = deltNode(root, 20)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 30")
root = deltNode(root, 30)
print("Inorder traversal of the modified tree")
inorder(root)

print("\nDelete 50")
root = deltNode(root, 50)
print("Inorder traversal of the modified tree")
inorder(root)

