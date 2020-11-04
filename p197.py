def BinarySearch(part, key):
    left = 0
    right = len(part) - 1

    while left <= right:
        mid = (left + right) // 2

        if part[mid] == key:
            return True

        elif part[mid] < key:
            left = mid + 1

        elif part[mid] > key:
            right = mid - 1

    return False

n = int(input())
part = input()
part = part.split(' ')
part.sort()

m = int(input())
require = input()
require = require.split(' ')

for i in range(0, n):
    part[i] = int(part[i])

for i in range(0, m):
    require[i] = int(require[i])

for i in range(0, m):
    if(BinarySearch(part, require[i])):
        print('yes', end=' ')

    else:
        print('no', end=' ')
