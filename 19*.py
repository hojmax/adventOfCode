import time
startTime = time.time()
rules = dict()
valid = []

def parse(key):
    output = []
    for e in rules[key]:
        if e.isalpha():
            output.append(e)
        elif " " in e:
            parts = e.split(" ")
            array1 = parse(parts[0])
            array2 = parse(parts[1])
            for e1 in array1:
                for e2 in array2:
                    output.append(e1+e2)
        else:
            output += parse(e)
    return output
        
with open("/Users/axelhojmark/Dropbox/CODE/AOC/rules.txt", 'r') as f:
    lines = f.read().splitlines()
    for line in lines:
        parts = line.split(": ")
        if "|" in parts[1]:
            rules[parts[0]] = parts[1].split(" | ")
        elif '"' in parts[1]:
            rules[parts[0]] = [parts[1][1]]
        else:
            rules[parts[0]] = [parts[1]]
    valid = set(parse("0"))
    
with open("/Users/axelhojmark/Dropbox/CODE/AOC/candidates.txt", 'r') as f:
    lines = f.read().splitlines()
    count = 0
    for line in lines:
        if line in valid:
            count += 1
    print(count)
                
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
