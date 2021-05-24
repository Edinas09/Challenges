#!/bin/python3
# Author: Edina Do Nascimento Silva
import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
class Game:
    def __init__(self, index, value, direction):
        self.index = index
        self.value = value
        self.direction = direction
        self.left = None if (index - 1) == -1 else (index - 1)
        self.right = (index + 1)
        self.twostepsright = (index + 2)

    def __contains__(self, item):
        return item == self.value

    def __repr__(self):
        return f"<index: {self.index} | value: {self.value} | left: {self.left} | right: {self.right} | direction: {self.direction}>"

    def update_game(self, index):
        self.direction = index

    def search_value(self, listgame, n, index):

        return self.value

    def make_game(c, n):
        listgame = []
        for index in range(n):
            value = c[index]
            # print(f"index: {index} | value: {value} ")
            game = Game(index, value, 0)
            listgame.append(game)
            # print(game.left)
            # print(listgame)

            counter = 0
            way = 0
        for index in range(n):
            # print(listgame[index])

            twostepspositon = listgame[index].twostepsright

            if twostepspositon < n:
                twostepspositon = listgame[twostepspositon].value
            else:
                twostepspositon = None

            if twostepspositon == 1:
                way = index + 1
            elif twostepspositon == 0:
                way = listgame[index].twostepsright

            listgame[index].direction = way

            #  como eu faço para fazer o update na lista no atributo da classe direction com o valor do way???



            #print(f"<index: {listgame[index].index} | value: {listgame[index].value} | left: {listgame[index].left} | right: {listgame[index].right} | twostepsright: {listgame[index].twostepsright} | twostepsrightvalue: {twostepspositon} | direction: {listgame[index].direction} | way: {way}>")
            # self.search_value(listgame[index].twostepsright)
        position = listgame[0].direction

        for index, grid in enumerate(listgame):

            if index == position:
                counter += 1
                position = grid.direction
        # print(f"<Contadorrrrr: {counter}")
        return counter


def jumpingOnClouds(c, n):
    listGame = Game.make_game(c, n)


    return listGame


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input())
    # c = list(map(int, input().rstrip().split()))
    n = 7
    c = (0, 0, 1, 0, 0, 1, 0)
    #c = (0, 0, 0, 0, 1, 0)
    result = jumpingOnClouds(c, n)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
