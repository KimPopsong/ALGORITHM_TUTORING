n = int(input())

s = input().split()

s = [int(i) for i in s]

fixedPoint = -1

left = 0
right = n - 1

while right >= left:
    mid = (left + right) // 2

    if mid == s[mid]:
        fixedPoint = mid
        break

    elif mid < s[mid]:
        right = mid - 1

    else:
        left = mid + 1

print(fixedPoint)
