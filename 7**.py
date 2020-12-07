import time
startTime = time.time()

target = "shiny gold bag"
bags = {" other bag":[]}
with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    for e in lines:
        splt = e.split("contain")
        key = splt[0][:-2]
        value = [] 
        for x in splt[1].split(","):
            name = x[3:-2] if x[-2:] == "s." else (x[3:-1] if x[-1] == "." or x[-1] == "s" else x[3:])
            number = 0
            if x[1].isnumeric():
                number = int(x[1])
            value.append([number,name])
        bags[key] = value

def inBag(bag):
    value = 0
    for e in bags[bag]:
        value += e[0] * inBag(e[1])
    return value + 1

# Again the outer most bag is not included, hence the -1
print(inBag(target)-1)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
