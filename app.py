#rows = 5
#columns = 4
#grid = [(1,1,0,0), (0,0,1,0),(0,0,0,0), (1,0,1,1), (1,1,1,1)  ]

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def resultado(rows, columns, grid):
    #print(rows)
    #print(columns)
    #print(grid)
    gridPositionCluster = ([])
    gridPositionClusterWays = {}
    id = 1

    # identificar a posicao de cada numero 1 no grid e criar uma nova list
    for ind, linha in enumerate(grid):
        for j, column in enumerate(linha):

            print(f'linha:{ind} - coluna:{j} - valor: {column}')

            if column == 1:
                gridPositionCluster.append([ind, j, 0])


                gridPositionClusterWays[id] = [
                                            {'value': column,
                                             'row': ind,
                                             'column': j,
                                             'cluster': 0,
                                             'neighbor': {
                                                 'rowRight': ind+1,
                                                 'rowLeft': ind-1,
                                                 'columnUpper': j+1,
                                                 'columnDown': j-1,
                                                 'value': 0
                                             }}]
                id = id + 1




    #print(gridPositionCluster)
    #print(gridPositionClusterWays)
    #print(gridPositionClusterWays)
    #print('...........................................')
if __name__ == '__main__':


    #n = int(input())
    #ar = list(map(int, input().rstrip().split()))
    rows = 5
    columns = 4
    grid = (
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    )

    result = resultado(rows, columns, grid)

    #fptr.write(str(result) + '\n')

    #fptr.close()
