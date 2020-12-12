import time
startTime = time.time()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    dX = 10
    dY = -1
    x = 0
    y = 0
    for e in lines:
        value = int(e[1:])
        if e[0] == "N":
            dY -= value
        elif e[0] == "S":
            dY += value
        elif e[0] == "E":
            dX += value
        elif e[0] == "W":
            dX -= value
        elif e[0] == "L":
            for i in range(value//90):
                temp = dX
                dX = dY
                dY = -temp
        elif e[0] == "R":
            for i in range(value//90):
                temp = dX
                dX = -dY
                dY = temp
        elif e[0] == "F":
            x += dX * value
            y += dY * value
    print(abs(x)+abs(y))

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
