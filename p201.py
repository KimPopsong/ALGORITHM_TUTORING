n = input()
n = n.split(' ')

require = int(n[1])
n = int(n[0])

rice = input()
rice = rice.split(' ')

rice = [int (i) for i in rice]

rice.sort(reverse=True)

height = rice[0]

for i in range(height, 0, -1):
    sum = 0

    for j in range(0, n):
        if rice[j] > i:
            sum += rice[j] - i

        else:
            break

    if sum >= require:
        print(i)
        break
