import time
startTime = time.time()

def validPart(part, length):
    txt = part[:3]
    if txt == "byr":
        return 1920 <= int(part.split(':')[1]) <= 2002
    elif txt == "iyr":
        return 2010 <= int(part.split(':')[1]) <= 2020
    elif txt == "eyr":
        return 2020 <= int(part.split(':')[1]) <= 2030
    elif txt == "hgt":
        if part[:-2].split(':')[1].isnumeric():
            hgt = int(part[:-2].split(':')[1])
            if (part[-2:]=="cm"):
                return 150 <= hgt <= 193
            else:
                return 59 <= hgt <= 76
        else:
            return False
    elif txt == "hcl":
        clr = part.split(':')[1]
        if len(clr) == 7 and clr[0] == '#':
            for i in range(1,len(clr)):
                if not ((48 <= ord(clr[i]) <= 57) or (97 <= ord(clr[i]) <= 102)):
                    return False
            return True
        else:
            return False
    elif txt == "ecl":
        possible = ["amb","blu","brn","gry","grn","hzl","oth"]
        crnt = part.split(':')[1]
        for e in possible:
            if crnt == e:
                return True
        return False
    elif txt == "pid":
        id = part.split(':')[1]
        if len(id) == 9:
            for i in range(1,len(id)):
                if not (48 <= ord(id[i]) <= 57):
                    return False
            return True
        else:
            return False
    elif txt == "cid":
        return length != 7

def isValid(passport):
    if len(passport) >= 7:
        for e in passport:
            if not validPart(e, len(passport)):
                return False
        return True
    else:
        return False


with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    count = 0
    i = 0
    while i < len(lines):
        arg = []
        j = 0
        while i + j < len(lines) and lines[i + j] != '':
            arg = arg + lines[i + j].split(" ")
            j += 1
        if isValid(arg):
            count += 1
        i = i + j + 1
    print(count)



print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
