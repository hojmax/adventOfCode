import time
startTime = time.time()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = list(map(int,f.read().splitlines()))
    top = len(lines)
    bottom = top - 2
    target = 393911906
    while bottom >= 0:
        while bottom >= 0 and sum(lines[bottom:top]) > target:
            top -= 1
            bottom = min(bottom,top - 2)
        while bottom >= 0 and sum(lines[bottom:top]) < target:
            bottom -= 1
        if sum(lines[bottom:top]) == target:
            print(min(lines[bottom:top]) + max(lines[bottom:top]))
            break
    
            
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
