file = [x.strip() for x in open("input")]

def check(l):
    f1 = l[1] - l[0]
    for i in range(len(l) - 1):
        dif = l[i + 1] - l[i]
        if f1 * dif <= 0 or abs(dif) < 1 or abs(dif) > 3:
            return False
    return True


def check2(l):
    if check(l):
        return True
    for i in range(len(l)):
        l2 = l[:i] + l[i + 1:]
        if check(l2):
            return True
    return False
    
    
    
    
reports = [list(map(int, line.split())) for line in file]
part1 = sum(check(x) for x in reports)
part2 = sum(check2(x) for x in reports)
print(part2)