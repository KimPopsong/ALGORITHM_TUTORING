n = int(input())

s = input().split()

s = [int(i) for i in s]

fixedPoint = -1

for i in range(0, n):
    if i == s[i]:
        fixedPoint = i
        break

print(fixedPoint)