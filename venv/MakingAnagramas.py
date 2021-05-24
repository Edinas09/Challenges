#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):


    list_a = Counter(a)
    list_b = Counter(b)

    countador_a = 0
    countador_b = 0
    resultado = 0

    for key, value in list_a.items():
        if key not in list_b:
            countador_b = countador_b + value

        if key in list_b and value > list_b[key]:
            countador_b = countador_b + value - list_b[key]


    for key, value in list_b.items():
        if key not in list_a:
            countador_a = countador_a + value

        if key in list_a and value > list_a[key]:
            countador_a = countador_a + value - list_a[key]

    print(countador_a)
    print(countador_b)

    resultado = countador_a + countador_b

    return resultado

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()
    b = input()

    res = makeAnagram(a, b)
    print(res)

    # fptr.write(str(res) + '\n')
    # fptr.close()
