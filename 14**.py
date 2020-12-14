import time
startTime = time.time()

permutations = dict()
// Jeg checkede filen og kunne se at der maks forekom 9 "floating bits". Derfor er 2**9 grænsen.
for i in range(2**9):
    permutations[i] = bin(i)[2:]

def getCombinations(appliedMask,floatingCount):
    global permutations
    output = []
    for i in range(2**floatingCount):
        fillIn = permutations[i].zfill(floatingCount)
        current = ""
        j = 0
        for i, e in enumerate(appliedMask):
            if e != "X":
                current += e
            else:
                current += fillIn[j]
                j += 1
        output.append(current)
    return output

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    mask = ""
    memory = dict()
    for e in lines:
        if e[:4] == "mask":
            mask = e[7:]
        elif e[:3] == "mem":
            key = int(e.split("[")[1].split("]")[0])
            value = int(e.split(" = ")[1])
            appliedMask = ""
            floatingCount = 0
            for i, e in enumerate('{0:036b}'.format(key)):
                if mask[i] != "0":
                    appliedMask += mask[i]
                    if mask[i] == "X":
                        floatingCount += 1
                else:
                    appliedMask += e
            combinations = getCombinations(appliedMask,floatingCount)
            for e in combinations:
                memory[int(e,2)] = value
    print(sum(memory.values()))
        

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
