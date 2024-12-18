filename = "test"
content = open(filename).read().strip()

def p1():
    out = ""
    n = 0
    for i in range(len(content)):
        if i % 2 == 0:
            out += str(n)*int(content[i])
            n += 1
        else:
            out += "."*int(content[i])
    
    indices = []
    for i in range(len(out)):
        if out[i] != ".": continue
        indices.append(i)
    
    out = [[x] for x in out]

    print(out)
    for i in indices:
        print(i)
        out[i] = out.pop(-1)
    
    print(out)
    pass


print(p1())