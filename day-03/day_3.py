# Didn't quite understand this question so i reached out for help.

chunk = []
with open("day-03/input.txt", "r") as f:
    for line in f:
        chunk.append(line)


xMax = int(len(chunk[0])-1)


def getAmountOfTreesOnSlope(xIncrement, yIncrement):
    posX = 0
    posY = 0
    trees = 0

    while posY < len(chunk):
        if chunk[posY][posX] == "#":
            trees += 1
        posX += xIncrement
        posY += yIncrement
        if posX >= xMax:
            posX -= xMax

    return trees


# Part 1
print("Trees: " + str(getAmountOfTreesOnSlope(3, 1)))

# Part 2
print("Trees: " + str((getAmountOfTreesOnSlope(1, 1) * getAmountOfTreesOnSlope(3, 1) *
                       getAmountOfTreesOnSlope(5, 1) * getAmountOfTreesOnSlope(7, 1) * getAmountOfTreesOnSlope(1, 2))))
