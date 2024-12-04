import sys

sys.path.append("/Users/nikolaiborbe/Documents/Programming/Advent-of-Code/src/")
from aoc_utils import *

filename = "input"
lines = [x.strip() for x in open(filename)]
# file = open(filename).read()


def p1():
    tot = 0
    # horizontal
    for i in range(len(lines)):
        for j in range(len(lines[0]) - 3):
            if lines[i][j:j+4] == "XMAS" or lines[i][j:j+4] == "SAMX":
                tot += 1
    # vertical
    for i in range(len(lines) - 3):
        for j in range(len(lines[0])):
            if lines[i][j] == "X" and lines[i+1][j] == "M" and lines[i+2][j] == "A" and lines[i+3][j] == "S":
                tot += 1
            elif lines[i][j] == "S" and lines[i+1][j] == "A" and lines[i+2][j] == "M" and lines[i+3][j] == "X":
                tot += 1
    # diagonal 1
    for i in range(len(lines) - 3):
        for j in range(len(lines[0]) - 3):
            if lines[i][j] == "X" and lines[i+1][j+1] == "M" and lines[i+2][j+2] == "A" and lines[i+3][j+3] == "S":
                tot += 1
            elif lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M" and lines[i+3][j+3] == "X":
                tot += 1
    # diagonal 2
    for i in range(len(lines) - 3):
        for j in range(3, len(lines[0])):
            if lines[i][j] == "X" and lines[i+1][j-1] == "M" and lines[i+2][j-2] == "A" and lines[i+3][j-3] == "S":
                tot += 1
            elif lines[i][j] == "S" and lines[i+1][j-1] == "A" and lines[i+2][j-2] == "M" and lines[i+3][j-3] == "X":
                tot += 1
    print(tot)


def p2():
    tot = 0
    for i in range(len(lines) - 2):
        for j in range(len(lines[0]) - 2):
            if (lines[i][j] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S" 
                and lines[i+2][j] == "M" and lines[i+1][j+1] == "A" and lines[i][j+2] == "S"):
                    tot += 1
            elif (lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M"
                and lines[i+2][j] == "S" and lines[i+1][j+1] == "A" and lines[i][j+2] == "M"):
                    tot += 1
            elif (lines[i][j] == "M" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "S"
                and lines[i+2][j] == "S" and lines[i+1][j+1] == "A" and lines[i][j+2] == "M"):
                    tot += 1
            elif (lines[i][j] == "S" and lines[i+1][j+1] == "A" and lines[i+2][j+2] == "M"
                and lines[i+2][j] == "M" and lines[i+1][j+1] == "A" and lines[i][j+2] == "S"):
                    tot += 1
    print(tot)

p1()
p2()
