class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

    def __repr__(self):
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



def set_level(root, level):
    root.level = level
    maxLevelRight = level
    maxLevelLeft = level

    if root.right:
        maxLevelRight = set_level(root.right, level + 1)

    if root.left:
        maxLevelLeft = set_level(root.left, level + 1)

    if maxLevelRight > maxLevelLeft:
        maxLevelres = maxLevelRight
    else:
        maxLevelres = maxLevelLeft

    return maxLevelres

def print_level(root, level):
    if root.level == level:
        print(root.info, end=" ")
    else:
        if root.left:
            print_level(root.left, level)
        if root.right:
            print_level(root.right, level)


def levelOrder(root):

    maxLevel = set_level(root, 1)


    for number in range(1, maxLevel+1):
        print_level(root, number)





tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])


levelOrder(tree.root)
