#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    hour_glass_list = []

    for linha in range(1,5):
        for coluna in range(1,5):

            print (" Voce esta na linha {} e na coluna {} do 2DArray".format(linha,coluna))
            miolo = int(arr[linha][coluna])

            mioloCima = int(arr[linha-1][coluna])
            mioloBaixo = int(arr[linha + 1][coluna])

            mioloCimaDireita = int(arr[linha-1][coluna+1])
            mioloCimaEsquerda = int(arr[linha-1][coluna-1])


            mioloBaixoDireita = int(arr[linha+1][coluna+1])

            mioloBaixoEsquerda = int(arr[linha+1][coluna-1])

            print(f" Miolo é : {miolo}")
            print(f" mioloCima é : {mioloCima}")
            print(f" mioloCimaDireita é : {mioloCimaDireita}")
            print(f" mioloCimaEsquerda é : {mioloCimaEsquerda}")
            print(f" mioloBaixo é : {mioloBaixo}")
            print(f" mioloBaixoDireita é : {mioloBaixoDireita}")
            print(f" mioloBaixoEsquerda é : {mioloBaixoEsquerda}")

            soma = miolo + mioloCima + mioloCimaDireita + mioloCimaEsquerda + mioloBaixo + mioloBaixoDireita + mioloBaixoEsquerda
            print(soma)
            hour_glass_list.append(soma)

    print(hour_glass_list)
    print(max(hour_glass_list))
    return max(hour_glass_list)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
