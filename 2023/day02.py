from pathlib import Path

def solvePuzzle(data, maxR, maxB, maxG):
    total1 = 0
    total2 = 0

    for game in data:
        possible = True
        minB = 0
        minR = 0
        minG = 0
        game = game.split(":")
        gameNo = int(game[0].split(" ")[1])
        game = game[1].strip().split(";")

        for diceSet in game:
            diceSet = diceSet.split(",")
            red = 0
            blue = 0
            green = 0
            for dice in diceSet:
                dice = dice.strip().split(" ")
                if dice[1] == "red":
                    red = int(dice[0])
                    minR = max(red, minR)
                elif dice[1] == "green":
                    green = int(dice[0])
                    minG = max(green, minG)
                else:
                    blue = int(dice[0])
                    minB = max(blue, minB)

            if red > maxR or green > maxG or blue > maxB:
                possible = False

        if possible:
            total1 += gameNo
        total2 += minB * minG * minR

    return "Total 1: " + str(total1) + "\nTotal 2: " + str(total2) 


txtName = Path(__file__).stem + ".txt"
file = open(txtName, "r")

maxRed = 12
maxGreen = 13
maxBlue = 14
print(solvePuzzle(file,maxRed,maxBlue,maxGreen))
