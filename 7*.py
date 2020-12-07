import time
startTime = time.time()

target = "shiny gold bag"
bags = {" other bag":[]}
doesContain = set()
doesNotContain = set()
allBags = set()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    for e in lines:
        splt = e.split("contain")
        allBags.add(splt[0][:-2])
        bags[splt[0][:-2]] = list(map(lambda x: x[3:-2] if x[-2:] == "s." else (x[3:-1] if x[-1] == "." or x[-1] == "s" else x[3:]), splt[1].split(",")))
        
def hasTarget(bag):
    if bag == target or bag in doesContain:
        return True
    elif bag in doesNotContain:
        return False
    else:
        for e in bags[bag]:
            if hasTarget(e):
                return True
        return False
        
for e in allBags:
    if hasTarget(e):
        doesContain.add(e)
    else:
        doesNotContain.add(e)

# Subtract one because "shiny gold bag" cannot contain itself
print(len(doesContain) - 1)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
