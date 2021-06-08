# Colocar o código/rascunho abaixo
# rows = 5
# columns = 4
# grid = [(1,1,0,0), (0,0,1,0),(0,0,0,0), (1,0,1,1), (1,1,1,1)  ]
# Amazon GO Stores

# !/bin/python3

import math
import os
import random
import re
import sys

class Block:
    def __init__(self, value, row, column):
        self.row = row
        self.column = column
        self.top = None
        self.left = None
        self.right = None
        self.down = None
        self.value = value
        self.is_cluster = True if value else False
        self.cluster_number = 0

    def set_cluster_number(self, number):
        if not self.is_cluster:
            return

        self.cluster_number = number

        self.top.set_cluster_number(number) if self.top and not self.top.cluster_number else None
        self.down.set_cluster_number(number) if self.down and not self.down.cluster_number else None
        self.right.set_cluster_number(number) if self.right and not self.right.cluster_number else None
        self.left.set_cluster_number(number) if self.left and not self.left.cluster_number else None




def create_grid(grid):
    """"
    1. Criar classes para cada posição
    2. Referenciar cada classe e seus vizinhos [top, down, left, right]
    3. Buscar se é cluster, recursivamente
    class:
    top -> None
    left -> None
    right -> classe
    down -> classe
    value -> int
    is_cluster bool -> true
    cluster_number int -> 1
    """
    for row_pos, row in enumerate(grid):
        for col_pos, col in enumerate(row):
            grid[row_pos][col_pos] = Block(col, row_pos, col_pos)

    for row_pos, row in enumerate(grid):
        for col_pos, col in enumerate(row):
            block = grid[row_pos][col_pos]
            block.left = grid[row_pos][col_pos - 1] if col_pos - 1 >= 0 else None
            block.right = grid[row_pos][col_pos + 1] if col_pos + 1 < len(row) else None
            block.top = grid[row_pos - 1][col_pos] if row_pos - 1 >= 0 else None
            block.down = grid[row_pos + 1][col_pos] if row_pos + 1 < len(grid) else None
    return grid


def count_custer_number(grid, custerNumber):
    for row in grid:
        for block in row:
            # se o bloco é cluster e não te, cluster number setado.
            if block.is_cluster and not block.cluster_number:
                block.set_cluster_number(custerNumber)

                custerNumber = custerNumber + 1

    return custerNumber - 1


if __name__ == '__main__':
    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    rows = 5
    columns = 4
    grid = (
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 1, 1],
        [1, 1, 1, 1],
    )

    # result = resultado(rows, columns, grid)
    gridBlock = create_grid(grid)
    # print(solucao)
    print(count_custer_number(gridBlock, 1))
    # fptr.write(str(result) + '\n')

    # fptr.close()


