import time
startTime = time.time()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    x = 0
    y = 0
    directions = [{"x":1,"y":0},
                  {"x":0,"y":1},
                  {"x":-1,"y":0},
                  {"x":0,"y":-1}]
    index = 0
    for e in lines:
        value = int(e[1:])
        if e[0] == "N":
            y -= value
        elif e[0] == "S":
            y += value
        elif e[0] == "E":
            x += value
        elif e[0] == "W":
            x -= value
        elif e[0] == "L":
            index -= value // 90
            while index < 0:
                index += len(directions)
        elif e[0] == "R":
            index += value // 90
            index %= len(directions)
        elif e[0] == "F":
            x += directions[index]["x"] * value
            y += directions[index]["y"] * value
    print(abs(x)+abs(y))

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
