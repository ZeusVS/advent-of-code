from collections import defaultdict
from pathlib import Path

def part1(data):
    data = data.split("\n")
    data.pop()
    total = 0
    for linePos in range(len(data)):
        number = 0
        isSurrounded = False
        for charPos in range(len(data[linePos])):
            if data[linePos][charPos].isdigit():
                number = number * 10 + int(data[linePos][charPos])
                minLinePos = max(linePos-1, 0)
                maxLinePos = min(linePos+2, len(data))
                minCharPos = max(charPos-1, 0)
                maxCharPos = min(charPos+2, len(data[linePos]))
                for i in range(minLinePos, maxLinePos):
                    for j in range(minCharPos, maxCharPos):
                       if data[i][j].isdigit() == False and data[i][j] != ".":
                            isSurrounded = True
            else:
                if isSurrounded == True:
                    total += number
                number = 0
                isSurrounded = False
        # If the last character of the line was a number we have to check again
        if isSurrounded == True:
            print(number)
            total += number

    return total
        
def part2(data):
    data = data.split("\n")
    data.pop()
    total = 0
    gears = defaultdict(list)
    for linePos in range(len(data)):
        number = 0
        isGear = False
        for charPos in range(len(data[linePos])):
            if data[linePos][charPos].isdigit():
                number = number * 10 + int(data[linePos][charPos])
                minLinePos = max(linePos-1, 0)
                maxLinePos = min(linePos+2, len(data))
                minCharPos = max(charPos-1, 0)
                maxCharPos = min(charPos+2, len(data[linePos]))
                for i in range(minLinePos, maxLinePos):
                    for j in range(minCharPos, maxCharPos):
                       if data[i][j] == "*":
                            isGear = True
                            gearNo = f"{i} + {j}"
            else:
                if isGear == True:
                    gears[gearNo].append(number)
                number = 0
                isGear = False
        # If the last character of the line was a number we have to check again
        if isGear == True:
            gears[gearNo].append(number)
    for value in gears.values():
        if len(value) == 2:
            total += value[0] * value[1]
    return total

txtName = Path(__file__).stem + ".txt"
file = open(txtName, "r")
file = file.read()

print(part1(file))
print(part2(file))

