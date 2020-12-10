import time
from functools import reduce
startTime = time.time()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = list(map(int,f.read().splitlines()))
    lines.sort()
    arrangements = [0] + lines + [lines[-1] + 3]
    expendables = [[],[]]
    for j in range(1,len(arrangements)-1):
        if arrangements[j+1]-arrangements[j-1] <= 3:
            expendables[0].append(j)
        if j-2 >= 0 and arrangements[j+1]-arrangements[j-2] <= 3:
            expendables[1].append([j-1,j])
    singles = expendables[0]
    i = 0
    partitions = []
    while i < len(singles):
        current = [singles[i]]
        j = i + 1
        while j < len(singles) and singles[j]-current[-1] == 1:
            current.append(singles[j])
            j += 1
        partitions.append(current)
        i = j
    binaryComb = {1:2,2:3,3:5}
    binaryParts = []
    for e in partitions:
        binaryParts.append(binaryComb[len(e)])
    for i in range(len(partitions)):
        for e in expendables[1]:
            if min(e) > max(partitions[i]):
                break
            if min(e) >= min(partitions[i]) and max(e) <= max(partitions[i]):
                binaryParts[i] += 1
    print(reduce(lambda x, y: x*y, binaryParts))

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
