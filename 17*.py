import time
startTime = time.time()

def getNeighbourCount(x,y,z,blocks):
    count = 0
    for dZ in range(-1,2):
        for dY in range(-1,2):
            for dX in range(-1,2):
                if not (dZ==dY==dX==0) and (x+dX,y+dY,z+dZ) in blocks:
                    count += 1
    return count
input = [
    [0,0,1,0,0,1,0,0],
    [0,1,1,1,0,0,1,0],
    [1,0,0,1,1,0,1,0],
    [1,0,1,0,1,0,1,0],
    [0,1,0,0,1,1,1,0],
    [0,0,0,0,0,1,0,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,0,0,0,1,0]
]
current = {}
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 1:
            current[(j,i,0)] = 1
xRange = [-1,len(input[0])]
yRange = [-1,len(input)]
zRange = [-1,1]
for i in range(6):
    next = {}
    for z in range(zRange[0],zRange[1]+1):
        for y in range(yRange[0],yRange[1]+1):
            for x in range(xRange[0],xRange[1]+1):
                neighbours = getNeighbourCount(x,y,z,current)
                if (x,y,z) in current:
                    if neighbours == 2 or neighbours == 3:
                        next[(x,y,z)] = 1
                else:
                    if neighbours == 3:
                        next[(x,y,z)] = 1
                        zRange[0] = min(zRange[0],z-1)
                        yRange[0] = min(yRange[0],y-1)
                        xRange[0] = min(xRange[0],x-1)
                        zRange[1] = max(zRange[1],z+1)
                        yRange[1] = max(yRange[1],y+1)
                        xRange[1] = max(xRange[1],x+1)
    current = next
print(len(current))
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
