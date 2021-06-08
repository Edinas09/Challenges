#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    list_arr = itertools.combinations(arr,2)
    # diferenca_anterior = float("inf")
    # list_set = set()
    #
    #
    # for item1, item2 in list_arr:
    #     diferenca = abs(item1 - item2)
    #     list_set.add(diferenca)
    #     if diferenca == 0:
    #         break
    #
    #     #
    #     #
    #     #
    #     # if diferenca < diferenca_anterior :
    #     #     diferenca_anterior = diferenca
    #     #     if diferenca == 0:
    #     #         break
    #
    # print(len(list_set))
    return min(itertools.starmap(lambda x, j: abs(x-j), list_arr))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
