import time
startTime = time.time()

lines = []
acc = 0
executedLines = set()

def runLine(index):
    global acc
    if index in executedLines:
        print(acc)
    elif index < len(lines):
        executedLines.add(index)
        cmd = lines[index].split(" ")[0]
        value = int(lines[index].split(" ")[1])
        if cmd == "acc":
            acc += value
            runLine(index + 1)
        elif cmd == "jmp":
            runLine(index + value)
        else:
            runLine(index + 1)
        

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    runLine(0)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
