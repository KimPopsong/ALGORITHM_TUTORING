def Check():
    count = 0
    global view
    view -= 1
    if view < 0:
        view = 3

    while count != 4:
        if view == 0:
            if gameMap[locationX - 1][locationY] == 0:  # the place where I didn't go
                return True

            else:
                view = 3
                count += 1
                continue

        elif view == 1:
            if gameMap[locationX][locationY + 1] == 0:  # the place where I didn't go
                return True

            else:
                view -= 1
                count += 1
                continue

        elif view == 2:
            if gameMap[locationX + 1][locationY] == 0:  # the place where I didn't go
                return True

            else:
                view -= 1
                count += 1
                continue

        else:
            if gameMap[locationX][locationY - 1] == 0:  # the place where I didn't go
                return True

            else:
                view -= 1
                count += 1
                continue

    return False

def Move(v):
    global locationX, locationY, cnt

    gameMap[locationX][locationY] = 2  # Where I stand before

    if v == 0:
        locationX = locationX - 1

    elif v == 1:
        locationY = locationY + 1

    elif v == 2:
        locationX = locationX + 1

    else:
        locationY = locationY - 1

    if gameMap[locationX][locationY] == 0:
            cnt += 1

def MoveBack():
    if view == 0:
        if gameMap[locationX + 1][locationY] == 2:
            Move(2)

        elif gameMap[locationX + 1][locationY] == 1:
            return False

    elif view == 1:
        if gameMap[locationX][locationY - 1] == 2:
            Move(3)

        elif gameMap[locationX][locationY - 1] == 1:
            return False

    elif view == 2:
        if gameMap[locationX - 1][locationY] == 2:
            Move(0)

        elif gameMap[locationX - 1][locationY] == 1:
            return False

    else:
        if gameMap[locationX][locationY + 1] == 2:
            Move(1)

        elif gameMap[locationX][locationY + 1] == 1:
            return False

    return True

mapSize = input().split()  # input n * m
mapSize = [int(i) for i in mapSize]

character = input().split()  # character's location and view
character = [int(i) for i in character]

gameMap = []  # saves the map

for i in range(mapSize[0]):
    temp = input().split()
    temp = [int(i) for i in temp]

    gameMap.append(temp)

locationX = character[0]
locationY = character[1]
view = character[2]

gameMap[locationX][locationY] = 2

cnt = 1

while True:
    if Check():
        Move(view)

    else:
        if MoveBack():
            continue

        else:
            print(cnt)
            break
