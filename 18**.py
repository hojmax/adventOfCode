import time
startTime = time.time()

def calculateValue(index, input):
    operater = "+"
    value = 0
    while index < len(input):
        if input[index].isnumeric():
            if operater == "+":
                value += int(input[index])
            elif operater == "*":
                value *= int(input[index])
        elif input[index] == ")":
            break
        elif input[index] == "(":
            if operater == "+":
                value += calculateValue(index+1,input)
            elif operater == "*":
                value *= calculateValue(index+1,input)
            balance = 1
            j = 1
            while balance != 0:
                if input[index+j] == ")":
                    balance -= 1
                elif input[index+j] == "(":
                    balance += 1
                j += 1
            index = index + j - 1
        elif input[index] == "+":
            operater = "+"
        elif input[index] == "*":
            operater = "*"
        index += 1
    return value

def addParentheses(input):
    chars = list(input)
    i = 0
    while i < len(chars):
        if chars[i] == "+":
            if chars[i-2].isnumeric():
                chars.insert(i-2,"(")
            else:  
                balance = -1
                j = -3
                while balance != 0:
                    if chars[i+j] == ")":
                        balance -= 1
                    elif chars[i+j] == "(":
                        balance += 1
                    j -= 1
                chars.insert(i + j + 1,"(")
            i += 1
            if chars[i+2].isnumeric():
                chars.insert(i+3,")")
            else:  
                balance = 1
                j = 3
                while balance != 0:
                    if chars[i+j] == ")":
                        balance -= 1
                    elif chars[i+j] == "(":
                        balance += 1
                    j += 1
                chars.insert(i + j,")")
        i += 1
    return "".join(chars)

with open("/Users/axelhojmark/Dropbox/CODE/AOC/input.txt", 'r') as f:
    lines = f.read().splitlines()
    sum = 0
    for line in lines:
        sum += calculateValue(0,addParentheses(line))
    print(sum)

print("**** Runtime: {} seconds ****".format(round(time.time() - startTime, 2)))
