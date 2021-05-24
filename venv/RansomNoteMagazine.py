#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    dic_magazine = Counter(magazine)

    print(dic_magazine)

    for palavra in note:

        #IMPORTANTE......

        # dic_magazine[]  SE A CHAVE NAO EXISTIR DA KEY ERRO
        #dic_magazine.get(palavra, 0) se não achar alteramos o padrao que None para 0
        dic_magazine[palavra] = dic_magazine.get(palavra, 0) - 1

        if dic_magazine.get(palavra, 0) == -1:
            return "No"

    return "Yes"




    # position = []
    # for notevalue in note:
    #     if notevalue in magazine:
    #         position.append(note.index(notevalue))
    #     else:
    #         return "No"
    #
    # for position in sorted(position, key=None, reverse=True):
    #     print("Position = {} | note {}".format(position, note))
    #     note.pop(position)
    #
    # if len(note) >= 1:
    #     return "No"
    # else:
    #     return "Yes"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
