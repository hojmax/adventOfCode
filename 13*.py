import time
import math
startTime = time.time()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    arrival = int(lines[0])
    busses = list(map(int,filter(lambda x: x != "x",lines[1].split(","))))
    bestWait = float("inf")
    bestBus = 0
    for bus in busses:
        currentWait = math.ceil(arrival/bus) * bus % arrival
        if currentWait < bestWait:
            bestWait = currentWait
            bestBus = bus
    print(bestBus * bestWait)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
