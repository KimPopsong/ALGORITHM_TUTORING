n = int(input())
number = []

for i in range(0, n):
    k = int(input())
    number.append(k)

for i in range(0, n - 1):
    for j in range(0, n - 1):
        if number[j] < number[j + 1]:
            number[j], number[j + 1] = number[j + 1], number[j]

for i in range(0, n):
    print(number[i], end=' ')