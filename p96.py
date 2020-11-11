import sys

s = sys.stdin.readline().split()

row = int(s[0])
col = int(s[1])

rows = []
minimum = []
maximum = 0

for i in range(0, row):
    temp = sys.stdin.readline().split()
    temp = [int(k) for k in temp]

    minimum.append(min(temp))
    rows.append(temp)

for i in range(0, row):
    if i == row - 1:
        temp = minimum[i]

    else:
        temp = max(minimum[i], minimum[i + 1])

    if temp > maximum:
        maximum = temp

print(maximum)
