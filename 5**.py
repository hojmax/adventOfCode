import time
startTime = time.time()

def binarySearch(lower,string):
    low = 0
    high = 2 ** len(string)
    for e in string:
        if e == lower:
            high = low + (high - low) / 2
        else:
            low = low + (high - low) / 2
    return low

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    allIds = []
    for e in lines:
        allIds.append(int(binarySearch("F",e[:7]) * 8 + binarySearch("L",e[7:])))
    allIds.sort()
    for i in range(0,len(allIds)-1):
        if allIds[i+1]-allIds[i] == 2:
            print(allIds[i],allIds[i+1])

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
