import sys
sys.path.append('/Users/nikolaiborbe/Documents/Programming/Advent-of-Code/src/')
from aoc_utils import *

filename = "input"
lines = [x.strip() for x in open(filename)]
#file = open(filename).read()

def g(target, lst):
    if len(lst) == 1:
        return target == lst[0]
    if target % lst[-1] == 0 and g(target // lst[-1], lst[:-1]):
        return True
    if target > lst[-1] and g(target - lst[-1], lst[:-1]):
        return True
    # part 2
    t = str(target)
    last = str(lst[-1])
    if (len(t) > len(last) and t.endswith(last) and
        g(int(t[:-len(last)]), lst[:-1])):
            return True

    return False
    

def p1():
    tot = 0
    for line in lines:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        if g(target, numbers):
            tot += target
        
    return tot

def p2():
    return p1()

print_(p2()) # print and copy answer to clipboard
