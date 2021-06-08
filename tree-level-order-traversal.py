class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelPrinter(node, resultado):

    if node is not None:
        if node.left is not None:
            nodeLeft = node.left
            resultado.append(nodeLeft.info)
            #resultado = resultado + nodeLeft
            #print(f"left:  {node.left}")
        if node.right is not None:
            nodeRight = node.right
            resultado.append(nodeRight.info)
            #resultado = resultado + nodeRight
            #print(f"right:  {node.right}")

        levelPrinter(node.left,resultado)
        levelPrinter(node.right,resultado)

    return resultado

def levelOrder(root):
    arr = [root.info]
    resultado = levelPrinter(root, arr)
    print(*resultado)
# Write your code here

tree = BinarySearchTree()
t = int(input())
arr = list(map(int, input().split()))

# t = 6 #int(input())
# arr = (1,2,5,3,6,4)
for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)