import time, random

s = input().split()

n = int(s[0])
find = s[1]



count = 0

s = input().split()

start = time.time()

for i in s:
    if i == find:
        count += 1

    elif i > find:
        break

if count:
    print(count)

else:
    print(-1)

end = start - time.time()
print('Time : ', end)