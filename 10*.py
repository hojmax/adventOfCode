import time
startTime = time.time()

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = list(map(int,f.read().splitlines()))
    lines.sort()
    differences = {1:0,2:0,3:1}
    differences[lines[0]] += 1
    for i in range(0,len(lines)-1):
        delta = lines[i+1]-lines[i]
        differences[delta] += 1
    print(differences)
            
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
