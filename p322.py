string = input()

sumNum = 0
stringList = []

for i in range(len(string)):
    if '1' <= string[i] <='9':
        sumNum += int(string[i])

    else:
        stringList.append(string[i])

stringList.sort()

for alpha in stringList:
    print(alpha, end='')

print(sumNum)
