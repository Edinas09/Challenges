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

    def set_level(self, level):
        self.level = level
        maxLevelRight = level
        maxLevelLeft = level

        if self.right:
            maxLevelRight = self.right.set_level(level + 1)

        if self.left:
            maxLevelLeft = self.left.set_level(level + 1)

        if maxLevelRight > maxLevelLeft:
            maxLevelres = maxLevelRight
        else:
            maxLevelres = maxLevelLeft

        return maxLevelres

    def print_level(self, level):
        if self.level == level:
            print(self.info, end=" ")
        else:
            if self.left:
                self.left.print_level(level)
            if self.right:
                self.right.print_level(level)





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
def listCreate(arvore, rootlist):
    if arvore:
        # rootlist.insert(0, arvore.info) de traz para frente
        rootlist.append([arvore.info, arvore.left, arvore.right])
        listCreate(arvore.left, rootlist)
        listCreate(arvore.right, rootlist)
    return rootlist

# def levelOrder(arvore, listroot):
#     # Root -> left -> right
#     if arvore:
#         listroot += str(arvore.info) + ""
#         listroot = levelOrder(arvore.left, listroot)
#         listroot = levelOrder(arvore.right, listroot)
#     return listroot


def levelOrder(root):

    maxLevel = root.set_level(1)
    # print(maxLevel)

    for number in range(1, maxLevel+1):
        root.print_level(number)

    # lista = []
    # listacriada = listCreate(root, lista)
    # print(listacriada)
    # res = str(listacriada[0][0]) + " "
    # for id_row, row in enumerate(listacriada):
    #     if listacriada[id_row][1] != None :
    #         left = str(listacriada[id_row][1]) + " "
    #     else:
    #         left = ""
    #
    #     if listacriada[id_row][2] != None :
    #         right = str(listacriada[id_row][2]) + " "
    #     else:
    #         right = ""
    #     res = res + left + right
    #
    # print(res)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])


levelOrder(tree.root)
