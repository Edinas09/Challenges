#!/bin/python3

# resposta uma list [0, 4]

import math
import os
import random
import re
import sys

#
# Complete the 'foo' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER flightDuration
#  2. INTEGER_ARRAY movieDuration
#

def foo(flightDuration, movieDuration):

    soma = 0
    listMovies = []

    flightDuration = flightDuration - 30

    print(movieDuration)

    for index, value in enumerate(movieDuration):
        for x in range(index+1,len(movieDuration)):
            soma = value + movieDuration[x]
            if int(soma) == int(flightDuration):
                # print(
                #     f"index: {index} | value: {value} | index_int: {x} | value: {movieDuration[x]} | soma: {soma} | flightDuration: {flightDuration}")
                listMovies.append([index, x])

    if not listMovies:
        return [-1,-1]
    elif len(listMovies) == 1:
        return listMovies[0]
    else:
        max_movie_geral = float('-inf')
        listreturn = []

        for index in listMovies:
            print(index)
            max_movie = max([movieDuration[x] for x in index])

            if max_movie > max_movie_geral:
                max_movie_geral = max_movie
                listreturn = index

        return listreturn



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    flightDuration = int(input().strip())

    movieDuration_count = int(input().strip())

    movieDuration = []

    for _ in range(movieDuration_count):
        movieDuration_item = int(input().strip())
        movieDuration.append(movieDuration_item)

    result = foo(flightDuration, movieDuration)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
