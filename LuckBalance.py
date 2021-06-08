#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'luckBalance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. 2D_INTEGER_ARRAY contests
#

def luckBalance(k, contests):
    # Write your code here
    print(contests)
    contador = 0
    total = 0
    list_contests = sorted(contests, reverse=True)
    print(list_contests)

    for index, value in list_contests:

        if value == 0:
            total = total + index
        elif contador < k:
            total = total + index
            contador = contador + 1
        else:
            total = total - index
    return total

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()