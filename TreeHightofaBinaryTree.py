class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __len__(self):
        return self.size()
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].info

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)

    def __iter__(self):
        return self


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def setLevel(self, level):
        self.root.level = level

    def printTree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "posorder":
            return self.posorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def preorder_print(self, start, traversal):
        #     "Root -> left -> Right"
        if start:
            traversal += (str(start.info) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        #     "Left -> Root -> Right"
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.info) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def posorder_print(self, start, traversal):
        #     "Left -> Right -> Root"
        if start:
            traversal = self.posorder_print(start.left, traversal)
            traversal = self.posorder_print(start.right, traversal)
            traversal += (str(start.info) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.info) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def create(self, val):
        level = 0
        # print("val = {}".format(val))
        if self.root == None:
            self.root = Node(val)
            self.root.level = level
        else:
            current = self.root
            level = int(self.root.level)
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    level = level + 1
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def height_two(root):

    if root is None:
        return -1
    left_height = height_two(root.left)
    right_height = height_two(root.right)
    return 1 + max(left_height, right_height)

tree = BinarySearchTree()

t = int(input())
arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(tree.printTree("preorder"))
print(tree.printTree("inorder"))
print(tree.printTree("posorder"))
print(tree.printTree("levelorder"))
print(tree.printTree("reverse_levelorder"))
print(tree.height(tree.root))
print(height_two(tree.root))
