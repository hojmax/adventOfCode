import time
startTime = time.time()

def slope(dX,dY):
    x = 0
    y = 0
    count = 0
    while y < len(lines):
        if lines[y][x % len(lines[y])] == '#':
            count += 1
        y += dY
        x += dX
    return count

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    print(slope(3,1))
        
    

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
