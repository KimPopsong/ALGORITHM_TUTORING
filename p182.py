n = input()

for i in range(0, len(n)):
    if(n[i] == ' '):
        k = int(n[i + 1:])
        n = int(n[:i])
        break

a = input()
b = input()

a = a.split(' ')
b = b.split(' ')

for i in range(0, n):
    a[i] = int(a[i])
    b[i] = int(b[i])

for i in range(0, n - 1):
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

        if b[j] < b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]

for i in range(0, k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]

print(sum(a))