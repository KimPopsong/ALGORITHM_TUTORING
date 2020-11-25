tileNumber = int(input())

dynamicTile = [0 for i in range(1001)]

dynamicTile[1] = 1
dynamicTile[2] = 3

for i in range(3, tileNumber + 1):
    dynamicTile[i] = (dynamicTile[i - 1] + 2 * dynamicTile[i - 2]) % 796796

print(dynamicTile[tileNumber])
