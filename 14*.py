import time
startTime = time.time()

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
            bitString = '{0:036b}'.format(value)
            outputString = ""
            for i in range(len(bitString)):
                if mask[i] != "X":
                    outputString += mask[i]
                else:
                    outputString += bitString[i]
            memory[key] = int(outputString,2)
    print(sum(memory.values()))
        

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
