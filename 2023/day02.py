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
            for dice in diceSet:
                dice = dice.strip().split(" ")
                if dice[1] == "red":
                    minR = max(minR, int(dice[0]))
                elif dice[1] == "green":
                    minG = max(minG, int(dice[0]))
                else:
                    minB = max(minB, int(dice[0]))

            if minR > maxR or minG > maxG or minB > maxB:
                possible = False

        if possible:
            total1 += gameNo
        total2 += minB * minG * minR

    return "Total 1: " + str(total1) + "\nTotal 2: " + str(total2) 


txtName = Path(__file__).stem + ".txt"
file = open(Path("input/"+txtName), "r")

maxRed = 12
maxGreen = 13
maxBlue = 14
print(solvePuzzle(file,maxRed,maxBlue,maxGreen))
