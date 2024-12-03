import re 

file = open("input").read()

def p1():
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = [list(map(int, (x, y))) for x, y in re.findall(pattern, file)]
    print(sum(x * y for x, y in matches))

def p2():
    do = True
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    matches = re.findall(pattern, file)
    new = []
    for i in matches:
        if i[0] == "do()":
            do = True
            continue
        elif i[0] == "don't()":
            do = False
            continue
        if do:
            new.append(int(i[1]) * int(i[2]))

    print(sum(new))

p1()
p2() 
