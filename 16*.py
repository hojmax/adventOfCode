import time
startTime = time.time()
rules = []

with open("/Users/axelhojmark/Dropbox/CODE/AOC/rules.txt", 'r') as f:
    lines = f.read().splitlines()
    for e in lines:
        rules += list(map(lambda x: list(map(int,x.split("-"))),e.split(": ")[1].split(" or ")))

with open("/Users/axelhojmark/Dropbox/CODE/AOC/tickets.txt", 'r') as f:
    tickets = list(map(lambda x: list(map(int,x.split(","))), f.read().splitlines()))
    error = 0
    for ticket in tickets:
        for value in ticket:
            isValid = False
            for rule in rules:
                if value >= rule[0] and value <= rule[1]:
                    isValid = True
                    break
            if not isValid:
                error += value
    print(error)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
