#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    count = 0
    # for i in range(0, len(a)):
    while count != d:
        # print(count)
        # print("entrou no loop")
        firstPosition = a[0]
        # print(f"Primeira posicao ===== {firstPosition}")
        a.remove(a[0])
        a.append(firstPosition)

        count = count + 1
        # print(f"Countador é {count}")
    return a

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])
    n = 5
    # d = int(nd[1])
    d = 4
    # a = list(map(int, input().rstrip().split()))
    a = [1, 2, 3, 4, 5]

    result = rotLeft(a, d)
    print(result)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
