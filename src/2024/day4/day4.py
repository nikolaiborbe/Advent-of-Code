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
            if lines[i][j : j + 4] == "XMAS" or lines[i][j : j + 4] == "SAMX":
                tot += 1
    # vertical
    for i in range(len(lines) - 3):
        for j in range(len(lines[0])):
            if [lines[i][j], lines[i + 1][j], lines[i + 2][j], lines[i + 3][j]] == [
                "X",
                "M",
                "A",
                "S",
            ] or [lines[i][j], lines[i + 1][j], lines[i + 2][j], lines[i + 3][j]] == [
                "S",
                "A",
                "M",
                "X",
            ]:
                tot += 1
    # diagonal
    for i in range(len(lines) - 3):
        for j in range(len(lines[0]) - 3):
            if [
                lines[i][j],
                lines[i + 1][j + 1],
                lines[i + 2][j + 2],
                lines[i + 3][j + 3],
            ] == ["X", "M", "A", "S"] or [
                lines[i][j],
                lines[i + 1][j + 1],
                lines[i + 2][j + 2],
                lines[i + 3][j + 3],
            ] == [
                "S",
                "A",
                "M",
                "X",
            ]:
                tot += 1
    # diagonal
    for i in range(len(lines) - 3):
        for j in range(3, len(lines[0])):
            if [
                lines[i][j],
                lines[i + 1][j - 1],
                lines[i + 2][j - 2],
                lines[i + 3][j - 3],
            ] == ["X", "M", "A", "S"] or [
                lines[i][j],
                lines[i + 1][j - 1],
                lines[i + 2][j - 2],
                lines[i + 3][j - 3],
            ] == [
                "S",
                "A",
                "M",
                "X",
            ]:
                tot += 1

    print(tot)


def p2():
    tot = 0
    for i in range(len(lines) - 2):
        for j in range(len(lines[0]) - 2):
            if [
                lines[i][j],
                lines[i+1][j+1],
                lines[i+2][j+2],
            ] == ["M", "A", "S"] and [
                lines[i+2][j],
                lines[i+1][j+1],
                lines[i][j+2],
            ] == ["M", "A", "S"]:
                tot += 1
            elif [
                lines[i][j],
                lines[i+1][j+1],
                lines[i+2][j+2],
            ] == ["S", "A", "M"] and [
                lines[i+2][j],
                lines[i+1][j+1],
                lines[i][j+2],
            ] == ["S", "A", "M"]:
                tot += 1
            elif [
                lines[i][j],
                lines[i+1][j+1],
                lines[i+2][j+2],
            ] == ["M", "A", "S"] and [
                lines[i][j+2],
                lines[i+1][j+1],
                lines[i+2][j],
            ] == ["M", "A", "S"]:
                tot += 1
            elif [
                lines[i][j],
                lines[i+1][j+1],
                lines[i+2][j+2],
            ] == ["S", "A", "M"] and [
                lines[i][j+2],
                lines[i+1][j+1],
                lines[i+2][j],
            ] == ["S", "A", "M"]:
                tot += 1
    print(tot)


p1()
p2()
