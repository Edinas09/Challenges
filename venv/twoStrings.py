#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    for index, value in enumerate(s1):

        for index_1, value_1 in enumerate(s2):
            # print(f" {index}  - {index_1} O valor de S1: {value} = S2: {value_1}")
            if value in value_1:
               # print("YES")
                return "YES"
                break
    # print("NO")
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())
    # q = [["hello", "world"], ["hi", "world]]

    for q_itr in range(q):
        s1 = input()
        s2 = input()

        result = twoStrings(s1, s2)
        print(result)

        # fptr.write(result + '\n')

    # fptr.close()
