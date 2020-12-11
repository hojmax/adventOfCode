import time
startTime = time.time()

def getFilledCount(i,j,grid):
    directions = [{"x":1,"y":1},
                  {"x":1,"y":0},
                  {"x":0,"y":1},
                  {"x":-1,"y":0},
                  {"x":0,"y":-1},
                  {"x":-1,"y":-1},
                  {"x":1,"y":-1},
                  {"x":-1,"y":1}]
    count = 0
    for dir in directions:
        k = 1
        while 0 <= i + dir["y"] * k < len(grid) and 0 <= j + dir["x"] * k < len(grid[i]):
            if grid[i + dir["y"] * k][j + dir["x"] * k] == "L":
                break
            elif grid[i + dir["y"] * k][j + dir["x"] * k] == "#":
                count += 1
                break
            k += 1
    return count

def simulate(grid):
    nextGrid = [[e for e in array] for array in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                filledCount = getFilledCount(i,j,grid)
                if grid[i][j] == "L" and filledCount == 0:
                    nextGrid[i][j] = "#"
                if grid[i][j] == "#" and filledCount >= 5:
                    nextGrid[i][j] = "L"
    return nextGrid
                
def print2d(grid):
    for e in grid:
        print("".join(e))

def countSeats(grid):
    count = 0
    for array in grid:
        for e in array:
            if e == "#":
                count += 1
    return count
    
with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    grid = []
    for e in lines:
        grid.append(list(e))
    for i in range(83):
        grid = simulate(grid)
    print(countSeats(grid))

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
