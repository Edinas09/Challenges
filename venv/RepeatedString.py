import math
import os
import random
import re
import sys


# Complete the repeatedString function below.
def repeatedString(s, n):
    char = len(s)  #3
    # remind = len(s) % n #1
    #
    # print(caract)
    # print(remind)
    # x = s * caract + s[:remind].count('a')
    count = 1
    listPosition = []
    timesrun = n / len(s)

    for pos, char in enumerate(s):
        if char == 'a':
            listPosition.append(pos)
    print(listPosition)

    # for num in n:
    #     for index, char in enumerate(listPosition):
    #         #x = listPosition[index] + char
    #         #print(x)
    #         #listPosition.append()



    return count

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = 'abca'

    # n = int(input())
    n = 10
    result = repeatedString(s, n)

    # fptr.write(str(result) + '\n')

    # fptr.close()
