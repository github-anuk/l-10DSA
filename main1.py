class Tree:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
def inorder(root):
    if root:
        if root.left is not None:
            inorder(root.left)
        print(root.data)
        if root.right is not None:
            inorder(root.right)

def insert(root,l):
    if root is None:
        return Tree(l)
    elif root.data >l:
        root.left = insert(root.left,l)
    else:
        root.right=insert(root.right,l)
    return root

def serch(root,m):
    if root.data==m:
        return root
    elif root.data >m and root.left is not None:
        return serch(root.left,m)
    elif root.data < m and root.right is not None:
        return serch(root.right,m)
    else:
        return -1
    
ml=int(input("ENTER HOW MUCH FOOD HAVE YOU GOT FOR TREE: "))
root=None
for i in range(ml):
    t=int(input("WHAT FOOD IS THAT YOU HAVE: "))
    root=insert(root,t)
inorder(root)
s=int(input("ENTER WHICH FOOD YOU WANT TO SEE IN TREES STOMACH: "))
se=serch(root,s)
if se == -1:
    print("NO SUCH FOOD IS FOUND IN TREE'S STOMACH ")
else:
    print("yes, TREE ATE ",se.data)