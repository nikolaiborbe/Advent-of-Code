file = [x.strip() for x in open("test")]

def part1():
    new_file = []
    for i in file:
        new_file.append([int(x) for x in i.split()])
    
    good = []
    for i in new_file:
        top_sort = sorted(i)
        bot_sort = sorted(i, reverse=True)
        if i == top_sort:
            good.append(i)
        elif i == bot_sort:
            good.append(i)
        
    good_list = 0
    for i in good:
        safe = True
        for j in range(1, len(i)):
            dif = abs(i[j-1] - i[j])
            if abs(i[j-1] - i[j]) > 3 or abs(i[j-1] - i[j]) == 0:
                safe = False
            else:
                pass
        if safe:
            good_list += 1
    return good_list
                
def part2():
    new_file = []
    for i in file:
        new_file.append([int(x) for x in i.split()])

    for i in range(len(new_file)-1, -1, -1):
        for j in range(1, len(new_file[i])):
            if abs(new_file[i][j] - new_file[i][j-1]) > 3:
                new_file.pop(i)
            else:
                pass

    count = 0
    for i in range(len(new_file)-1, -1, -1):
        if new_file[i][0] < new_file[i][-1]:
            incr = True
        else:
            incr = False

        index = False
        for j in range(1, len(new_file[i])):
            if incr:
                if new_file[i][j-1] >= new_file[i][j]:
                    index = j
                    break
            if not incr:
                if new_file[i][j-1] <= new_file[i][j]:
                    index = j
                    break
        if index != False:
            holder = new_file[i]
            holder.pop(index)
            if holder == sorted(holder):
                count += 1
    print(count)
            
        



    
        

part2()
            

        