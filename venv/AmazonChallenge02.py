#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#
class Robot:

    movement_rules = {"N":(0, 1),
                      "S":(0, -1),
                      "O":(-1, 0),
                      "L":(0, 1),}

    face_rules = {"L": {
        "N": "O",
        "O": "S",
        "S": "L",
        "L": "N",
    },
    "R": {
        "N": "L",
        "L": "S",
        "S": "O",
        "O": "N"
    },}

    def __init__ (self):
        self.face = "N"
        self.xposition = 0
        self.yposition = 0

    def move(self, command):
        if command == "G":
            x, y = self.movement_rules[self.face]
            self.xposition = self.xposition + x
            self.yposition += y
        else:
            self.face = self.face_rules[command][self.face]


def doesCircleExist(commands):
    # Write your code here
    for comm in commands:
        robot = Robot()
        yes = False
        for i in range(10):

            for x in comm:

                robot.move(x)

            if robot.xposition == 0 and robot.yposition == 0:
                print("YES")
                yes = True
                break

        if not yes:
            print("NO")



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    commands_count = int(input().strip())

    commands = []

    for _ in range(commands_count):
        commands_item = input()
        commands.append(commands_item)


    result = doesCircleExist(commands)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()
