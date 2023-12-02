fullBag = {'red': 12, 'blue': 14, 'green': 13}


def findAllInString(a: str, toFind: str):
    if not len(toFind) == 1:
        raise RuntimeError('toFind is not a single character')
    pos = []
    for i in range(len(a)):
        if a[i].__eq__(toFind):
            pos.append(i)
    return pos


with open('input/input2.txt') as f:
    lines = f.readlines()

total = 0
totalPow = 0
for line in lines:
    colPos = line.find(':')
    gameId = int(line[5:colPos])
    subGames = []
    semiPos = findAllInString(line, ';')
    minimumBalls = {'red': 0, 'green': 0, 'blue': 0}
    # add colon Pos into semiPos list for easy access with index -1
    semiPos.append(colPos)
    for i in range(len(semiPos) - 1):
        subGames.append(line[semiPos[i - 1] + 1:semiPos[i]])

    # add last game, last game is not ended with semicolon
    subGames.append(line[semiPos[-2] + 1:len(line)])
    ignoreGame = False
    for subGame in subGames:
        commaPos = findAllInString(subGame, ',')
        commaPos.append(len(subGame))
        commaPos.append(0)
        currHand = {'red': 0, 'blue': 0, 'green': 0}
        for i in range(len(commaPos) - 1):
            balls = subGame[commaPos[i - 1] + 1:commaPos[i]]
            for key in fullBag.keys():
                colorPos = balls.find(key)
                if not colorPos == -1:
                    currHand[key] += int(balls[0:colorPos])

        for key in fullBag.keys():
            if currHand[key] > fullBag[key]:
                ignoreGame = True
            if currHand[key] > minimumBalls[key]:
                minimumBalls[key] = currHand[key]

    if not ignoreGame:
        total += gameId

    prod = 1
    for val in minimumBalls.values():
        prod *= val
    totalPow += prod

print(total)
print(totalPow)
