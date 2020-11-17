s = input()

s = [int(i) for i in s]

sumNum = s[0]

for i in s[1:]:
    if sumNum == 0 or i == 0:
        sumNum += i

    else:
        sumNum *= i

print(sumNum)
