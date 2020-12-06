import time
startTime = time.time()

def uniqueCount(letters):
    count = set()
    for e in letters:
        count.add(e)
    return len(count)

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    count = 0
    i = 0
    while i < len(lines):
        arg = []
        j = 0
        while i + j < len(lines) and lines[i + j] != '':
            arg = arg + list(lines[i + j])
            j += 1
        count += uniqueCount(arg)
        i = i + j + 1
    print(count)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
