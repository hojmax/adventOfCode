import time
startTime = time.time()

def simulate(grid):
    nextGrid = [[e for e in array] for array in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                filledCount = 0
                for a in range(-1,2):
                    if 0 <= a+i < len(grid):
                        for b in range(-1,2):
                            if (a == 0 and b == 0) or not (0 <= b+j < len(grid[i])):
                                continue
                            if grid[a+i][b+j] == "#":
                                filledCount += 1
                if grid[i][j] == "L" and filledCount == 0:
                    nextGrid[i][j] = "#"
                if grid[i][j] == "#" and filledCount >= 4: 
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
    for i in range(110):
        grid = simulate(grid)
    print(countSeats(grid))

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
