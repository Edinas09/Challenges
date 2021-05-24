#!/bin/python3
# Author: Edina Do Nascimento Silva

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    contador = 0
    # loop lista
    listset = set(ar)
    # print(listset)
    for num in listset:
        quantidade = ar.count(num)
        divisao = quantidade // 2

        contador += divisao

    return contador
    # count
    # ar.count()

    # % 0 ou 1
    # add contador todos que deram 0.


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    n = 7
    ar = (1, 2, 1, 2, 1, 3, 2, 4, 3)
    result = sockMerchant(n, ar)
    print(f"how many pairs of socks: {result} ")
    #fptr.write(str(result) + '\n')

    #fptr.close()
