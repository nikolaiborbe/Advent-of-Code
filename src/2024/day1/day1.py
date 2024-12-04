# part 1
def part1():
    tot = 0

    left = []
    right = []
    with open ("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            arr = line.split()
            left.append(arr[0])
            right.append(arr[1])

    left.sort()
    right.sort()

    for i in range(len(left)):
        tot += abs(int(left[i]) - int(right[i]))


# part 2
def part2():
    score = 0

    count = {}
    left = []
    right = []
    with open ("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            arr = line.split()
            left.append(arr[0])
            right.append(arr[1])
    
    left = [int(i) for i in left]
    right = [int(i) for i in right]

    for i in range(len(left)):
        if left[i] not in count:
            count[left[i]] = 0
            
    for i in range(len(right)):
        if right[i] in count:
            count[right[i]] += 1

    similiarity_score = []
    for key in count:
        similiarity_score.append(key * count[key])
        
    print(sum(similiarity_score))

