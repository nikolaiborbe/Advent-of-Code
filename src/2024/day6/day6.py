import sys
sys.path.append('/Users/nikolaiborbe/Documents/Programming/Advent-of-Code/src/')
from aoc_utils import *

filename = "input"
house = list(map(list, open(filename).read().splitlines()))

def p1():
    for r in range(len(house)):
        for c in range(len(house[r])):
            if house[r][c] == "^":
                guard_row, guard_column = r, c
                break
        else:
            continue
        break

    dr, dc = -1, 0
    visited = set()

    while True:
        visited.add((guard_row, guard_column))
        if guard_row + dr < 0 or guard_column + dc < 0: break
        if guard_row + dr >= len(house) or guard_column + dc >= len(house[0]): break

        if house[guard_row + dr][guard_column + dc] == "#":
            dr, dc = dc, -dr
        else:
            guard_row += dr
            guard_column += dc
        
    return len(visited)


def p2():
    # i have no idea
    pass

print_(p1()) # print and copy answer to clipboard
