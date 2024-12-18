import math

filename = "input"
lines = [x.strip() for x in open(filename)]
map = [[x for x in line] for line in lines]
size = (len(map), len(map[0]))
antennas = dict()

for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] != ".":
            if map[r][c] not in antennas:
                antennas[map[r][c]] = [(r, c)]
            elif map[r][c] in antennas:
                antennas[map[r][c]].append((r, c))


def p1():
    antinodes = set()
    # for each node, set node as origo, find offset coordinates for
    # matching node, calculate distance, convert back to standard 
    # coordinates, if in range add 1 to count
    for freq in antennas:
        for cors in antennas[freq]:
            current = cors
            for match in antennas[freq]:
                if match == current: continue
                offset = (match[0] - current[0], match[1] - current[1])
                pos_offset = (offset[0]*2, offset[1]*2)
                neg_offset = (-offset[0], -offset[1])
                pos_antinode = (pos_offset[0]+current[0], pos_offset[1]+current[1])
                neg_antinode = [neg_offset[0]+current[0], neg_offset[1]+current[1]]
                if (0 <= pos_antinode[0] < size[0]) and (0 <= pos_antinode[1] < size[1]):
                    antinodes.add((pos_antinode[0], pos_antinode[1]))
                if (size[0] >= neg_antinode[0] >= size[0]) and (size[1] >= neg_antinode[1] >= size[1]):
                    antinodes.add((neg_antinode[0], neg_antinode[1]))
    return len(antinodes)
        
        
def p2():
    antinodes = set()
    for freq in antennas:
        for cors in antennas[freq]:
            current = cors
            for match in antennas[freq]:
                if match == current: continue
                offset = (match[0] - current[0], match[1] - current[1])
                dr, dc = offset[0], offset[1]
                x, y  = (current[0]+dr, current[1]+dc)
                while (0 <= x < size[0]) and (0 <= y < size[1]):
                    node = ((x, y))
                    antinodes.add((node))
                    x += dr
                    y += dc

                x, y  = (current[0]+dr, current[1]+dc)
                while (0 <= x < size[0]) and (0 <= y < size[1]):
                    node = ((x, y))
                    antinodes.add((node))
                    x -= dr
                    y -= dc

    return len(antinodes)

print(p2())
