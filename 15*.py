import time
startTime = time.time()

lastSaid = {14:1,
             3:2,
             1:3,
             0:4,
             9:5}
current = 5
index = 6
limit = 2020
while index < limit:
    if current in lastSaid:
        temp = lastSaid[current]
        lastSaid[current] = index
        current = index - temp
    else:
        lastSaid[current] = index
        current = 0
    index += 1

print(current)        

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
