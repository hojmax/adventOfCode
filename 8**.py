import time
startTime = time.time()

acc = 0

def runLine(executedLines, acc, index, lines):
    if index in executedLines:
        pass
    elif index < len(lines):
        executedLines.add(index)
        cmd = lines[index].split(" ")[0]
        value = int(lines[index].split(" ")[1])
        if cmd == "acc":
            runLine(executedLines, acc + value, index + 1, lines)
        elif cmd == "jmp":
            runLine(executedLines, acc, index + value, lines)
        else:
            runLine(executedLines, acc, index + 1, lines)
    else:
        print("TERMINATED CORRECTLY: %s"%acc)

def createAll(lines):
    output = []
    for i in range(len(lines)):
        if lines[i][:3] == "jmp":
            next = [e for e in lines]
            next[i] = "nop +1"
            output.append(next)
    return output

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    delta = createAll(lines)
    for e in delta:
        runLine(set(),0, 0, e)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
