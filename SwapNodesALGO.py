#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

class Node:
    def __init__(self, value, level):
        self.value = value
        self.level = level
        self.left = None
        self.right = None
    def __repr__(self):
        return f"<Value: {self.value} | level: {self.level} >"

def create_nodes(indexes):
    node = Node(1,1)
    list_node = [node]
    fila = deque()
    fila.append(node)

    for left, right in indexes:
        node = fila.popleft()
        if left != -1:
            node.left = Node(left, node.level+1)
            list_node.append(node.left)
            fila.append(node.left)
        if right != -1:
            node.right = Node(right, node.level+1)
            list_node.append(node.right)
            fila.append(node.right)
    return list_node

def swapNodes(indexes, queries):
    # Write your code here
    result = create_nodes(indexes)
    print(result[0].right)
    print(result[0].left)
    print(result[1].right)
    print(result[1].left)
    print(result[2].right)
    print(result[2].left)
    print(indexes)
    print(queries)
    return result
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    print(result)

    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')

    # fptr.close()
