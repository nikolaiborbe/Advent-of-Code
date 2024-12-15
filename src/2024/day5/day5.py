import sys
sys.path.append('/Users/nikolaiborbe/Documents/Programming/Advent-of-Code/src/')
from aoc_utils import *
import functools

filename = "input"
lines = [x.strip() for x in open(filename)]
#file = open(filename).read()

top, bottom = lines[:lines.index("")], lines[lines.index("")+1:]

rules = [tuple(map(int, x.split("|"))) for x in top]
numbers = [list(map(int, x.split(","))) for x in bottom]


def p1():
    out = []
    for i in range(len(numbers)):
        legal = True
        for j in range(1, len(numbers[i])):
            if (numbers[i][j-1], numbers[i][j]) not in rules: 
                legal = False
                break

        if legal: out.append(numbers[i])
    
    d = 0
    for i in range(len(out)):
        d += out[i][(len(out[i]))//2]

    return d
        
        

def p2():
    out = []
    not_legal = []

    for i in range(len(numbers)):
        legal = True
        for j in range(1, len(numbers[i])):
            if (numbers[i][j-1], numbers[i][j]) not in rules: 
                legal = False
                not_legal.append(numbers[i])
                break

        if legal: out.append(numbers[i])
    
    def s(x, y):
        if (x, y) in rules:
            return 1
        if (x, y) not in rules:
            return -1
        return 0


    d = 0
    for i in range(len(not_legal)):
        not_legal[i].sort(key=functools.cmp_to_key(s))
        d += not_legal[i][(len(not_legal[i])//2)]

    return d

print_(p2()) # print and copy answer to clipboard
