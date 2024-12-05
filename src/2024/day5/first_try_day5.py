import sys
sys.path.append('/Users/nikolaiborbe/Documents/Programming/Advent-of-Code/src/')
from aoc_utils import *

filename = "test.txt"
lines = [x.strip() for x in open(filename)]
#file = open(filename).read()


def p1():
    rules = []
    for l in lines:
        if l == "":
            break
        rules.append(tuple(map(int, l.split("|"))))

    pages = []
    found = False
    for l in lines:
        if found:
            pages.append(list(int(l) for l in l.split(",")))
        if l == "":
            found = True
    for line in pages:
        for i, j in zip(line, line[1:]): 
            for rule in rules:
                if (i, j) == rule:
                    
        

def p2():
    pass


ans = p1()
#ans = p2()


print_(ans) # print and copy answer to clipboard
