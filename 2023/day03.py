from collections import defaultdict
from pathlib import Path

def solvePuzzle(data):
    data = data.split("\n")
    data.pop()
    total1 = 0
    total2 = 0
    gears = defaultdict(list)
    for linePos in range(len(data)):
        number = 0
        isSurrounded = False
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
                        if data[i][j].isdigit() == False and data[i][j] != ".":
                            isSurrounded = True
            else:
                if isSurrounded == True:
                    total1 += number
                if isGear == True:
                    gears[gearNo].append(number)
                number = 0
                isGear = False
                isSurrounded = False
        # If the last character of the line was a number we have to check again
        if isSurrounded == True:
            total1 += number
        if isGear == True:
            gears[gearNo].append(number)
    for value in gears.values():
        if len(value) == 2:
            total2 += value[0] * value[1]
 
    return f"Total 1: {total1}\nTotal 2: {total2}"
       
txtName = Path(__file__).stem + ".txt"
file = open(Path("input/"+txtName), "r")

file = file.read()

print(solvePuzzle(file))

