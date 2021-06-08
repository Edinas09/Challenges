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


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
def update_level(node, level):
    level_count = level + 1

    if node is None:

        return level
    else:
        node.level = level_count
        level_count_left = update_level(node.left, level_count)
        level_count_right = update_level(node.right, level_count)
        print(f"< left: {node.left} | right: {node.right} | level: {node.level} >")
        if level_count_left > level_count_right:

            return level_count_left
        else:

            return level_count_right



def height(root):
    root.level = 0



    height_left = update_level(root.left, root.level) #2 , 0
    height_right = update_level(root.right, root.level) #5 , 0

    if height_left > height_right:
        return height_left
    else:
        return height_right

tree = BinarySearchTree()
t = 7 #int(input())

arr = (3,5,2,1,4,6,7)#list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])


print(height(tree.root))
