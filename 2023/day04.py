from pathlib import Path

def solvePuzzle(data):
    lines = len(data.readlines())
    cards = [1] * lines
    data.seek(0)

    total1 = 0
    for card in data:
        cardNo = int(card.split(":")[0].split()[-1]) - 1
        winningCards = card.split(":")[1].split("|")[1].split()
        myCards = card.split(":")[1].split("|")[0].split()
        points1 = 0
        points2 = 0
        for myCard in myCards:
            if myCard in winningCards:
                points2 += 1
                cards[cardNo + points2] += cards[cardNo]
                if points1 == 0:
                    points1 = 1
                else:
                    points1 *= 2
        # calculate the total for part 1
        total1 += points1
        # calculate the total for part 2

    total2 = sum(cards)
    return f"Total 1: {total1}\nTotal2 : {total2}"

txtName = Path(__file__).stem + ".txt"
file = open(Path("input/"+txtName), "r")

print(solvePuzzle(file))
