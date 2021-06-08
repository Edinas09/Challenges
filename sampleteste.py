#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'arraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def arraySum(numbers):
    # Write your code here

    sum = 0

    for number in numbers:
        sum = sum + number

    return sum

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    result = arraySum(numbers)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
