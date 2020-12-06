import time
startTime = time.time()

def isValid(passport):
    if len(passport) == 8:
        return True
    elif len(passport) == 7:
        for e in passport:
            if e[:3] == "cid":
                return False
        return True
    else:
        return False

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    count = 0
    i = 0
    while i < len(lines):
        arg = []
        j = 0
        while i + j < len(lines) and lines[i + j] != '':
            arg = arg + lines[i + j].split(" ")
            j += 1
        if isValid(arg):
            count += 1
        i = i + j + 1
    print(count)
        
    

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
