import time
startTime = time.time()
rules = {}
possible = {}
tickets = []

with open("/Users/axelhojmark/Dropbox/CODE/AOC/rules.txt", 'r') as f:
    lines = f.read().splitlines()
    for e in lines:
        rules[e.split(": ")[0]] = list(map(lambda x: list(map(int,x.split("-"))),e.split(": ")[1].split(" or ")))

with open("/Users/axelhojmark/Dropbox/CODE/AOC/tickets.txt", 'r') as f:
    tickets = list(map(lambda x: list(map(int,x.split(","))), f.read().splitlines()))
    # Removing false tickets
    for i in range(len(tickets)-1,-1,-1):
        for value in tickets[i]:
            isValid = False
            for rule in rules.values():
                for limits in rule:
                    if limits[0] <= value <= limits[1]:
                        isValid = True
                        break
                if isValid:
                    break
            if not isValid:
                tickets.pop(i)
                break
    # Filling possibilities
    for key in rules.keys():
        possible[key] = [True for i in range(20)]
    # Brute exclution of possibilities
    for key in possible.keys():
        for i in range(20):
            isValid = True
            for ticket in tickets:
                foundMatchingRule = False
                for limits in rules[key]:
                    if limits[0] <= ticket[i] <= limits[1]:
                        foundMatchingRule = True
                        break
                if not foundMatchingRule:
                    isValid = False
                    break
            if not isValid:
                possible[key][i] = False
    # Logical solving
    for i in range(7):
        for key1, value1 in possible.items():
            if value1.count(True) == 1:
                index = value1.index(True)
                for key2, value2 in possible.items():
                    if key2 != key1:
                        value2[index] = False
    # Finding result
    ticket = [101,71,193,97,131,179,73,53,79,67,181,89,191,137,163,83,139,127,59,61]
    mult = 1
    for key, value in possible.items():
        if key[:9] == "departure":
            mult *= ticket[value.index(True)]
    print(mult)
print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
