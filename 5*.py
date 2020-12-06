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
    highest = 0
    for e in lines:
        val = binarySearch("F",e[:7]) * 8 + binarySearch("L",e[7:])
        if val > highest:
            highest = val
    print(highest)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
