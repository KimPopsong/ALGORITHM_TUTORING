number = int(input())

numList = [0 for i in range(number + 1)]

for i in range(2, number + 1):
    numList[i] = numList[i - 1] + 1

    if i % 5 == 0 and numList[i] > numList[i // 5] + 1:
        numList[i] = numList[i // 5] + 1

    if i % 3 == 0 and numList[i] > numList[i // 3] + 1:
        numList[i] = numList[i // 3] + 1

    if i % 2 == 0 and numList[i] > numList[i // 2] + 1:
        numList[i] = numList[i // 2] + 1

print(numList[number])
