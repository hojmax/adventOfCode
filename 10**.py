import time
from functools import reduce
startTime = time.time()

def getRemovables(lines):
    removable = {"singles":[],"doubles":[]}
    adapters = [0] + lines + [lines[-1] + 3]
    for j in range(1,len(adapters)-1):
        if adapters[j+1]-adapters[j-1] <= 3:
            removable["singles"].append(j)
        if j-2 >= 0 and adapters[j+1]-adapters[j-2] <= 3:
            removable["doubles"].append([j-1,j])
    return removable
    
def getPartitions(removable):
    i = 0
    partitions = []
    while i < len(removable["singles"]):
        current = [removable["singles"][i]]
        j = i + 1
        while j < len(removable["singles"]) and removable["singles"][j]-current[-1] == 1:
            current.append(removable["singles"][j])
            j += 1
        partitions.append(current)
        i = j
    return partitions
    
with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = list(map(int,f.read().splitlines()))
    lines.sort()
    removable = getRemovables(lines)
    partitions = getPartitions(removable)
    partitionPossibilities = {1: 2,
                              2: 3,
                              3: 5}
    actualPossibilities = [partitionPossibilities[len(e)] for e in partitions]
    for i in range(len(partitions)):
        for e in removable["doubles"]:
            if min(e) > max(partitions[i]):
                break
            if min(e) >= min(partitions[i]) and max(e) <= max(partitions[i]):
                actualPossibilities[i] += 1
    combinations = reduce(lambda x, y: x*y, actualPossibilities)
    print(combinations)
 
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
