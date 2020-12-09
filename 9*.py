import time
startTime = time.time()

def isValid(num,parts):
    for i in range(0,len(parts)):
        for j in range(i+1,len(parts)):
            if parts[i] + parts[j] == num:
                return True
    return False

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = list(map(int,f.read().splitlines()))
    for i in range(25,len(lines)):
        if not isValid(lines[i],lines[i-25:i]):
            print(lines[i])
            
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
